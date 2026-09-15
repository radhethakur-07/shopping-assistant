from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import or_, func

from . import models, schemas


# =============================================================================
# Product CRUD Operations
# =============================================================================

def get_products(db: Session, skip: int = 0, limit: int = 100, category: Optional[str] = None) -> List[models.Product]:
    query = db.query(models.Product)
    if category:
        query = query.filter(models.Product.category.ilike(category))
    return query.order_by(models.Product.id.asc()).offset(skip).limit(limit).all()


def get_product(db: Session, product_id: int) -> Optional[models.Product]:
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def search_products(db: Session, query_str: str) -> List[models.Product]:
    if not query_str or not query_str.strip():
        return []
    term = f"%{query_str.strip()}%"
    return db.query(models.Product).filter(
        or_(
            models.Product.name.ilike(term),
            models.Product.brand.ilike(term),
            models.Product.category.ilike(term),
            models.Product.description.ilike(term),
        )
    ).all()


def get_products_by_category(db: Session, category: str) -> List[models.Product]:
    return db.query(models.Product).filter(models.Product.category.ilike(category.strip())).all()


def create_product(db: Session, product_in: schemas.ProductCreate) -> models.Product:
    db_product = models.Product(**product_in.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, product_id: int, product_in: schemas.ProductUpdate) -> Optional[models.Product]:
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    update_data = product_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_product, field, value)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int) -> bool:
    db_product = get_product(db, product_id)
    if not db_product:
        return False
    db.delete(db_product)
    db.commit()
    return True


# =============================================================================
# Cart CRUD Operations
# =============================================================================

def get_or_create_cart(db: Session, cart_id: int = 1) -> models.Cart:
    cart = db.query(models.Cart).filter(models.Cart.id == cart_id).first()
    if not cart:
        cart = models.Cart(id=cart_id)
        db.add(cart)
        db.commit()
        db.refresh(cart)
    return cart


def add_item_to_cart(db: Session, cart_id: int, product_id: int, quantity: int = 1) -> models.CartItem:
    cart = get_or_create_cart(db, cart_id)
    product = get_product(db, product_id)
    if not product:
        raise ValueError(f"Product with ID {product_id} does not exist.")
    if product.stock_quantity <= 0:
        raise ValueError(f"Product '{product.name}' is currently out of stock.")

    # Check if item already in cart
    existing_item = db.query(models.CartItem).filter(
        models.CartItem.cart_id == cart.id,
        models.CartItem.product_id == product_id
    ).first()

    if existing_item:
        new_quantity = existing_item.quantity + quantity
        if new_quantity > product.stock_quantity:
            new_quantity = product.stock_quantity
        existing_item.quantity = new_quantity
        db.commit()
        db.refresh(existing_item)
        return existing_item
    else:
        actual_qty = min(quantity, product.stock_quantity)
        cart_item = models.CartItem(
            cart_id=cart.id,
            product_id=product_id,
            quantity=actual_qty
        )
        db.add(cart_item)
        db.commit()
        db.refresh(cart_item)
        return cart_item


def update_cart_item(db: Session, item_id: int, quantity: int) -> Optional[models.CartItem]:
    item = db.query(models.CartItem).filter(models.CartItem.id == item_id).first()
    if not item:
        return None
    product = get_product(db, item.product_id)
    if not product:
        return None
    if quantity <= 0:
        db.delete(item)
        db.commit()
        return None
    
    item.quantity = min(quantity, product.stock_quantity if product.stock_quantity > 0 else 1)
    db.commit()
    db.refresh(item)
    return item


def remove_cart_item(db: Session, item_id: int) -> bool:
    item = db.query(models.CartItem).filter(models.CartItem.id == item_id).first()
    if not item:
        return False
    db.delete(item)
    db.commit()
    return True


def clear_cart(db: Session, cart_id: int = 1) -> bool:
    cart = get_or_create_cart(db, cart_id)
    db.query(models.CartItem).filter(models.CartItem.cart_id == cart.id).delete()
    db.commit()
    return True


def format_cart_response(cart: models.Cart) -> dict:
    subtotal = 0.0
    total_quantity = 0
    formatted_items = []

    for item in cart.items:
        if item.product:
            item_subtotal = round(item.product.price * item.quantity, 2)
            subtotal += item_subtotal
            total_quantity += item.quantity
            formatted_items.append({
                "id": item.id,
                "cart_id": item.cart_id,
                "product_id": item.product_id,
                "quantity": item.quantity,
                "product": item.product,
                "subtotal": item_subtotal
            })

    subtotal = round(subtotal, 2)
    tax = round(subtotal * 0.05, 2)  # 5% estimated tax
    total_price = round(subtotal + tax, 2)

    return {
        "id": cart.id,
        "created_at": cart.created_at,
        "items": formatted_items,
        "item_count": len(formatted_items),
        "total_quantity": total_quantity,
        "subtotal": subtotal,
        "tax": tax,
        "total_price": total_price
    }


# =============================================================================
# Shopping List CRUD Operations
# =============================================================================

def get_or_create_shopping_list(db: Session, list_id: int = 1) -> models.ShoppingList:
    s_list = db.query(models.ShoppingList).filter(models.ShoppingList.id == list_id).first()
    if not s_list:
        s_list = models.ShoppingList(id=list_id, name="My Shopping List")
        db.add(s_list)
        db.commit()
        db.refresh(s_list)
    return s_list


def add_item_to_shopping_list(db: Session, list_id: int, product_id: int, quantity: int = 1) -> models.ShoppingListItem:
    s_list = get_or_create_shopping_list(db, list_id)
    product = get_product(db, product_id)
    if not product:
        raise ValueError(f"Product with ID {product_id} does not exist.")

    # If product already in list, increase quantity
    existing_item = db.query(models.ShoppingListItem).filter(
        models.ShoppingListItem.shopping_list_id == s_list.id,
        models.ShoppingListItem.product_id == product_id
    ).first()

    if existing_item:
        existing_item.quantity += quantity
        existing_item.purchased = False  # Reset purchased status if re-adding
        db.commit()
        db.refresh(existing_item)
        return existing_item
    else:
        list_item = models.ShoppingListItem(
            shopping_list_id=s_list.id,
            product_id=product_id,
            quantity=quantity,
            purchased=False
        )
        db.add(list_item)
        db.commit()
        db.refresh(list_item)
        return list_item


def update_shopping_list_item(db: Session, item_id: int, quantity: Optional[int] = None, purchased: Optional[bool] = None) -> Optional[models.ShoppingListItem]:
    item = db.query(models.ShoppingListItem).filter(models.ShoppingListItem.id == item_id).first()
    if not item:
        return None
    if quantity is not None:
        if quantity <= 0:
            db.delete(item)
            db.commit()
            return None
        item.quantity = quantity
    if purchased is not None:
        item.purchased = purchased
    db.commit()
    db.refresh(item)
    return item


def toggle_shopping_list_item_purchased(db: Session, item_id: int, purchased: bool) -> Optional[models.ShoppingListItem]:
    return update_shopping_list_item(db, item_id=item_id, purchased=purchased)


def remove_shopping_list_item(db: Session, item_id: int) -> bool:
    item = db.query(models.ShoppingListItem).filter(models.ShoppingListItem.id == item_id).first()
    if not item:
        return False
    db.delete(item)
    db.commit()
    return True


def clear_shopping_list(db: Session, list_id: int = 1) -> bool:
    s_list = get_or_create_shopping_list(db, list_id)
    db.query(models.ShoppingListItem).filter(models.ShoppingListItem.shopping_list_id == s_list.id).delete()
    db.commit()
    return True


def format_shopping_list_response(s_list: models.ShoppingList) -> dict:
    items = s_list.items or []
    total_items = len(items)
    purchased_items = sum(1 for item in items if item.purchased)
    pending_items = total_items - purchased_items
    completion_percentage = round((purchased_items / total_items * 100), 1) if total_items > 0 else 0.0

    return {
        "id": s_list.id,
        "name": s_list.name,
        "created_at": s_list.created_at,
        "items": items,
        "total_items": total_items,
        "purchased_items": purchased_items,
        "pending_items": pending_items,
        "completion_percentage": completion_percentage
    }
