import os
import sys

sys.path.insert(0, os.path.abspath("backend"))

from app.database import SessionLocal, engine, Base
from seed import seed_database
from app import crud, models, recommendations

def run_tests():
    print("--- Starting SmartCart Verification Tests ---")
    
    # 1. Test Database Creation & Seeding
    db = SessionLocal()
    count = seed_database(db, force=True)
    print(f"[TEST 1] Seeded {count} products successfully.")
    assert count >= 40, f"Expected at least 40 products, got {count}"

    # 2. Test Categories
    categories = db.query(models.Product.category).distinct().all()
    cat_names = [c[0] for c in categories]
    print(f"[TEST 2] Found categories: {cat_names}")
    assert len(cat_names) >= 10, f"Expected at least 10 categories, got {len(cat_names)}"

    # 3. Test Search
    pasta_prods = crud.search_products(db, "pasta")
    print(f"[TEST 3] Search for 'pasta' returned {len(pasta_prods)} results: {[p.name for p in pasta_prods]}")
    assert len(pasta_prods) > 0, "Search for pasta returned 0 results"

    # 4. Test Cart Operations
    cart = crud.get_or_create_cart(db, cart_id=1)
    crud.clear_cart(db, cart_id=1)
    pasta_item = pasta_prods[0]
    crud.add_item_to_cart(db, cart_id=1, product_id=pasta_item.id, quantity=2)
    cart_resp = crud.format_cart_response(crud.get_or_create_cart(db, cart_id=1))
    print(f"[TEST 4] Cart subtotal: {cart_resp['subtotal']}, items: {cart_resp['item_count']}, total qty: {cart_resp['total_quantity']}")
    assert cart_resp['total_quantity'] == 2
    assert cart_resp['subtotal'] > 0

    # 5. Test Recommendations with Pasta in Cart
    recs = recommendations.calculate_recommendations(db, cart_id=1, limit=5)
    print(f"[TEST 5] Generated {len(recs.recommendations)} recommendations for cart:")
    for r in recs.recommendations:
        print(f"   -> {r.product.name} ({r.score*100:.0f}% match) [{r.recommendation_type}]: {r.reason}")
    assert len(recs.recommendations) > 0
    assert any(r.recommendation_type in ['complementary', 'category_affinity', 'popular'] for r in recs.recommendations)

    # 6. Test Shopping List Operations
    s_list = crud.get_or_create_shopping_list(db, list_id=1)
    crud.clear_shopping_list(db, list_id=1)
    bread_matches = crud.search_products(db, "bread")
    milk_matches = crud.search_products(db, "milk")
    assert len(bread_matches) > 0 and len(milk_matches) > 0
    bread = bread_matches[0]
    milk = milk_matches[0]
    item1 = crud.add_item_to_shopping_list(db, list_id=1, product_id=bread.id, quantity=1)
    item2 = crud.add_item_to_shopping_list(db, list_id=1, product_id=milk.id, quantity=2)
    crud.toggle_shopping_list_item_purchased(db, item_id=item1.id, purchased=True)
    list_resp = crud.format_shopping_list_response(crud.get_or_create_shopping_list(db, list_id=1))
    print(f"[TEST 6] Shopping list: {list_resp['purchased_items']}/{list_resp['total_items']} purchased ({list_resp['completion_percentage']}%)")
    assert list_resp['total_items'] == 2
    assert list_resp['purchased_items'] == 1
    assert list_resp['completion_percentage'] == 50.0

    # 7. Test FastAPI Endpoints via TestClient
    from fastapi.testclient import TestClient
    from app.main import app

    client = TestClient(app)

    # 7.1 Health
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "ok"
    print("[API 1] /health: PASS")

    # 7.2 Products
    res = client.get("/api/products?limit=10")
    assert res.status_code == 200
    prods = res.json()
    assert len(prods) > 0
    print(f"[API 2] /api/products: PASS ({len(prods)} products retrieved)")

    # 7.3 Search
    res = client.get("/api/products/search?q=apple")
    assert res.status_code == 200
    print(f"[API 3] /api/products/search?q=apple: PASS ({len(res.json())} items found)")

    # 7.4 Cart
    res = client.post("/api/cart/items", json={"product_id": prods[0]["id"], "quantity": 3})
    assert res.status_code == 201
    c_data = res.json()
    assert c_data["total_quantity"] >= 3
    print(f"[API 4] POST /api/cart/items: PASS (subtotal = {c_data['subtotal']})")

    # 7.5 Recommendations
    res = client.get("/api/recommendations?cart_id=1&limit=4")
    assert res.status_code == 200
    rec_data = res.json()
    assert len(rec_data["recommendations"]) > 0
    print(f"[API 5] GET /api/recommendations: PASS ({len(rec_data['recommendations'])} items returned)")

    # 7.6 Shopping List
    res = client.post("/api/shopping-list/items", json={"product_id": prods[1]["id"], "quantity": 2})
    assert res.status_code == 201
    sl_data = res.json()
    assert sl_data["total_items"] > 0
    print(f"[API 6] POST /api/shopping-list/items: PASS ({sl_data['total_items']} items in list)")

    print("\n>>> ALL AUTOMATED TESTS & REST APIS PASSED WITH 100% SUCCESS! <<<")

if __name__ == "__main__":
    run_tests()
