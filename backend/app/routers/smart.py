"""
SmartCart AI Assistant Router
Powers:
1. Recipe-to-Cart Meal Bundles
2. Live Cart Health & Nutrition Score Analyzer
3. Predictive 'Did You Forget?' Basket Reminders
4. Conversational SmartBot Assistant
"""

from typing import Dict, List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

from .. import crud, models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/smart",
    tags=["Smart Assistant"]
)


# =============================================================================
# Curated Recipe Knowledge Base
# =============================================================================
RECIPES = [
    {
        "id": "pasta-marinara",
        "name": "Classic Italian Penne Marinara",
        "category": "Dinner",
        "prep_time": "15 Mins",
        "difficulty": "Easy",
        "description": "Rich slow-simmered plum tomato marinara with Penne Rigate, extra virgin olive oil, and aged parmesan.",
        "image_url": "https://images.unsplash.com/photo-1551462147-ff29053bfc14?auto=format&fit=crop&w=600&q=80",
        "target_keywords": ["penne", "marinara", "parmesan", "olive oil", "garlic"]
    },
    {
        "id": "breakfast-toast-jam",
        "name": "Golden Butter Toast with Strawberry Jam",
        "category": "Breakfast",
        "prep_time": "5 Mins",
        "difficulty": "Easy",
        "description": "Warm toasted whole wheat bread generously layered with creamy salted butter and sweet strawberry jam.",
        "image_url": "https://images.unsplash.com/photo-1533089860892-a7c6f0a88666?auto=format&fit=crop&w=600&q=80",
        "target_keywords": ["bread", "butter", "jam", "milk"]
    },
    {
        "id": "dal-rice-bowl",
        "name": "Comforting Moong Dal & Basmati Rice",
        "category": "Lunch & Dinner",
        "prep_time": "25 Mins",
        "difficulty": "Easy",
        "description": "Protein-rich aromatic yellow moong dal tempered with golden turmeric and garlic, served over fluffy Basmati rice.",
        "image_url": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=600&q=80",
        "target_keywords": ["rice", "dal", "turmeric", "onions", "cooking oil"]
    },
    {
        "id": "protein-power-breakfast",
        "name": "High-Protein Scramble & Avocado Toast",
        "category": "Fitness & Breakfast",
        "prep_time": "10 Mins",
        "difficulty": "Easy",
        "description": "Fluffy free-range eggs with creamy avocado on toasted artisan sourdough, paired with Greek yogurt.",
        "image_url": "https://images.unsplash.com/photo-1525351484163-7529414344d8?auto=format&fit=crop&w=600&q=80",
        "target_keywords": ["eggs", "avocado", "sourdough", "yogurt"]
    },
    {
        "id": "chai-tea-break",
        "name": "English Breakfast Tea & Crunchy Biscuits",
        "category": "Snacks & Refreshment",
        "prep_time": "5 Mins",
        "difficulty": "Quick",
        "description": "A steaming cup of robust breakfast tea brewed with fresh milk, cane sugar, and classic wheat digestive biscuits.",
        "image_url": "https://images.unsplash.com/photo-1576092768241-dec231879fc3?auto=format&fit=crop&w=600&q=80",
        "target_keywords": ["tea", "milk", "sugar", "biscuits"]
    }
]


# =============================================================================
# Schemas
# =============================================================================
class ChatMessage(BaseModel):
    message: str


# =============================================================================
# 1. Recipe Endpoints
# =============================================================================
@router.get("/recipes", summary="Get curated recipes with cart match analysis")
def get_smart_recipes(
    cart_id: int = Query(1, ge=1),
    db: Session = Depends(get_db)
):
    """
    Returns curated recipes and checks which ingredients are already in the user's cart
    vs which items are missing, along with bundle pricing.
    """
    cart = crud.get_or_create_cart(db, cart_id=cart_id)
    cart_product_names = [ci.product.name.lower() for ci in cart.items if ci.product]

    all_products = db.query(models.Product).filter(models.Product.stock_quantity > 0).all()

    recipe_responses = []

    for r in RECIPES:
        in_cart_items = []
        missing_products = []
        missing_cost = 0.0

        for kw in r["target_keywords"]:
            # Find best product in store matching kw
            matching_product = None
            for p in all_products:
                if kw in p.name.lower() or kw in p.category.lower():
                    matching_product = p
                    break

            if matching_product:
                # Check if in cart
                in_cart = any(kw in cp_name for cp_name in cart_product_names)
                if in_cart:
                    in_cart_items.append(schemas.ProductResponse.model_validate(matching_product))
                else:
                    missing_products.append(schemas.ProductResponse.model_validate(matching_product))
                    missing_cost += matching_product.price

        recipe_responses.append({
            "id": r["id"],
            "name": r["name"],
            "category": r["category"],
            "prep_time": r["prep_time"],
            "difficulty": r["difficulty"],
            "description": r["description"],
            "image_url": r["image_url"],
            "total_ingredients_count": len(r["target_keywords"]),
            "in_cart_count": len(in_cart_items),
            "missing_count": len(missing_products),
            "is_complete": len(missing_products) == 0,
            "missing_bundle_price": round(missing_cost, 2),
            "missing_products": missing_products,
            "in_cart_products": in_cart_items
        })

    return {"recipes": recipe_responses}


@router.post("/recipes/{recipe_id}/add-to-cart", summary="1-Click add missing recipe items to cart")
def add_recipe_to_cart(
    recipe_id: str,
    cart_id: int = Query(1, ge=1),
    db: Session = Depends(get_db)
):
    """Adds all missing ingredients for a recipe directly into the cart."""
    recipe = next((r for r in RECIPES if r["id"] == recipe_id), None)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found.")

    cart = crud.get_or_create_cart(db, cart_id=cart_id)
    cart_product_ids = {ci.product_id for ci in cart.items}

    all_products = db.query(models.Product).filter(models.Product.stock_quantity > 0).all()
    added_count = 0

    for kw in recipe["target_keywords"]:
        for p in all_products:
            if kw in p.name.lower():
                if p.id not in cart_product_ids:
                    crud.add_item_to_cart(db, cart_id=cart_id, product_id=p.id, quantity=1)
                    cart_product_ids.add(p.id)
                    added_count += 1
                break

    updated_cart = crud.get_or_create_cart(db, cart_id=cart_id)
    return {
        "status": "success",
        "message": f"Added {added_count} ingredients for '{recipe['name']}' to your cart.",
        "cart": crud.format_cart_response(updated_cart)
    }


# =============================================================================
# 2. Cart Health & Nutrition Radar
# =============================================================================
@router.get("/cart-health", summary="Analyze cart health and nutrition metrics")
def get_cart_health(
    cart_id: int = Query(1, ge=1),
    db: Session = Depends(get_db)
):
    """
    Computes a comprehensive Health & Diet Score (0-100) based on cart contents,
    analyzing the balance of fresh produce, protein, and processed snacks.
    """
    cart = crud.get_or_create_cart(db, cart_id=cart_id)
    if not cart.items:
        return {
            "health_score": 0,
            "status_label": "Empty Basket",
            "produce_pct": 0,
            "protein_pct": 0,
            "snack_pct": 0,
            "summary": "Add items to your cart to see real-time nutritional insights.",
            "tips": ["Start by adding fresh fruits and vegetables for dietary fiber."]
        }

    total_qty = sum(ci.quantity for ci in cart.items)
    produce_qty = 0
    protein_qty = 0
    snack_qty = 0

    for ci in cart.items:
        cat = ci.product.category if ci.product else ""
        qty = ci.quantity
        if cat in ["Fruits", "Vegetables"]:
            produce_qty += qty
        elif cat in ["Dairy", "Grains"]:
            protein_qty += qty
        elif cat in ["Snacks", "Frozen Food"]:
            snack_qty += qty

    produce_pct = round((produce_qty / total_qty) * 100)
    protein_pct = round((protein_qty / total_qty) * 100)
    snack_pct = round((snack_qty / total_qty) * 100)

    # Health score algorithm: base 50 + produce bonus + protein balance - heavy snack penalty
    raw_score = 50 + (produce_pct * 0.40) + (protein_pct * 0.20) - (snack_pct * 0.35)
    health_score = max(10, min(100, round(raw_score)))

    if health_score >= 80:
        label = "Excellent Balanced Diet"
    elif health_score >= 60:
        label = "Good Nutritional Balance"
    elif health_score >= 40:
        label = "Moderate (High in Carbs/Snacks)"
    else:
        label = "Needs More Fresh Produce"

    tips = []
    if produce_pct < 30:
        tips.append("🥦 Your cart is low on fresh vegetables and fruits. Adding Apples, Carrots, or Spinach will boost daily vitamins.")
    if snack_pct > 35:
        tips.append("🍪 Snack items make up a large portion of your basket. Consider swapping chips with California Almonds or Greek Yogurt.")
    if protein_pct >= 25 and produce_pct >= 30:
        tips.append("🌟 Great nutritional balance! You have a wholesome mix of protein staples and fresh fiber.")

    if not tips:
        tips.append("✅ Well-rounded grocery selection for healthy weekly meals.")

    return {
        "health_score": health_score,
        "status_label": label,
        "produce_pct": produce_pct,
        "protein_pct": protein_pct,
        "snack_pct": snack_pct,
        "summary": f"Your current cart holds {total_qty} items with {produce_pct}% fresh produce.",
        "tips": tips
    }


# =============================================================================
# 3. Predictive 'Did You Forget?' Reminders
# =============================================================================
@router.get("/did-you-forget", summary="Predictive reminders for missing essentials")
def get_did_you_forget(
    cart_id: int = Query(1, ge=1),
    db: Session = Depends(get_db)
):
    """
    Analyzes current cart contents to identify critical missing companion items
    and provides 1-click reminders.
    """
    cart = crud.get_or_create_cart(db, cart_id=cart_id)
    if not cart.items:
        return {"reminders": []}

    cart_names = " ".join([ci.product.name.lower() for ci in cart.items if ci.product])
    all_products = db.query(models.Product).filter(models.Product.stock_quantity > 0).all()

    reminders = []

    # Rule 1: Jam without Bread / Butter
    if "jam" in cart_names and not any(k in cart_names for k in ["bread", "sourdough", "croissant"]):
        bread = next((p for p in all_products if "bread" in p.name.lower()), None)
        if bread:
            reminders.append({
                "trigger_item": "Strawberry Jam",
                "message": "You added Strawberry Jam! Did you forget Whole Wheat Bread or Butter for toast?",
                "suggested_product": schemas.ProductResponse.model_validate(bread)
            })

    # Rule 2: Pasta without Pasta Sauce
    if "pasta" in cart_names and "sauce" not in cart_names and "marinara" not in cart_names:
        sauce = next((p for p in all_products if "sauce" in p.name.lower() or "marinara" in p.name.lower()), None)
        if sauce:
            reminders.append({
                "trigger_item": "Italian Pasta",
                "message": "You have Penne Pasta in your cart! Did you forget Marinara Pasta Sauce?",
                "suggested_product": schemas.ProductResponse.model_validate(sauce)
            })

    # Rule 3: Tea without Milk or Sugar
    if "tea" in cart_names and "milk" not in cart_names:
        milk = next((p for p in all_products if "milk" in p.name.lower()), None)
        if milk:
            reminders.append({
                "trigger_item": "English Breakfast Tea",
                "message": "Brewing morning tea? You might need Fresh Whole Milk or Sugar.",
                "suggested_product": schemas.ProductResponse.model_validate(milk)
            })

    # Rule 4: Rice without Dal
    if "rice" in cart_names and "dal" not in cart_names and "lentils" not in cart_names:
        dal = next((p for p in all_products if "dal" in p.name.lower()), None)
        if dal:
            reminders.append({
                "trigger_item": "Basmati Rice",
                "message": "Making rice for dinner? Don't forget Yellow Moong Dal for a wholesome meal.",
                "suggested_product": schemas.ProductResponse.model_validate(dal)
            })

    return {"reminders": reminders[:2]}


# =============================================================================
# 4. Floating SmartBot AI Chatbot
# =============================================================================
@router.post("/chat", summary="Conversational AI Assistant query processor")
def chat_with_assistant(
    chat_in: ChatMessage,
    db: Session = Depends(get_db)
):
    """
    Parses natural language requests and returns relevant grocery recommendations,
    recipe kits, and instant add actions.
    """
    msg = chat_in.message.lower().strip()
    all_products = db.query(models.Product).filter(models.Product.stock_quantity > 0).all()

    # 1. Budget Queries (e.g., "under $10", "$15")
    if "under" in msg or "budget" in msg or "$" in msg or "cheap" in msg:
        cheap_staples = [p for p in all_products if p.price <= 3.50][:4]
        return {
            "reply": "Here are our best budget-friendly staple picks under $3.50 each:",
            "products": [schemas.ProductResponse.model_validate(p) for p in cheap_staples],
            "action": "view_budget"
        }

    # 2. Breakfast & Morning queries
    if "breakfast" in msg or "morning" in msg or "tea" in msg or "coffee" in msg:
        b_items = [p for p in all_products if any(k in p.name.lower() for k in ["bread", "butter", "jam", "eggs", "tea", "oats"])][:4]
        return {
            "reply": "Here is a classic morning breakfast setup (Eggs, Bread, Butter, and Tea):",
            "products": [schemas.ProductResponse.model_validate(p) for p in b_items],
            "action": "view_breakfast"
        }

    # 3. Protein & Health queries
    if "protein" in msg or "healthy" in msg or "diet" in msg or "fit" in msg:
        health_items = [p for p in all_products if any(k in p.name.lower() for k in ["yogurt", "eggs", "almonds", "dal", "spinach", "oats"])][:4]
        return {
            "reply": "Here are top high-protein and nutrient-rich staples to power your day:",
            "products": [schemas.ProductResponse.model_validate(p) for p in health_items],
            "action": "view_protein"
        }

    # 4. Dinner / Pasta / Cooking queries
    if "dinner" in msg or "pasta" in msg or "cook" in msg or "recipe" in msg:
        dinner_items = [p for p in all_products if any(k in p.name.lower() for k in ["pasta", "marinara", "parmesan", "garlic", "olive oil"])][:4]
        return {
            "reply": "I suggest cooking a delicious Penne Marinara dinner! Here are the core ingredients:",
            "products": [schemas.ProductResponse.model_validate(p) for p in dinner_items],
            "action": "view_recipe"
        }

    # Default fallback search
    matching = [p for p in all_products if any(word in p.name.lower() for word in msg.split() if len(word) > 2)][:4]
    if not matching:
        matching = all_products[:4]

    return {
        "reply": f"Here is what I found for '{chat_in.message}':",
        "products": [schemas.ProductResponse.model_validate(p) for p in matching],
        "action": "general_search"
    }
