from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)


@router.get("", response_model=schemas.CartResponse, summary="Get cart details")
def get_cart(
    cart_id: int = Query(1, ge=1, description="Cart ID"),
    db: Session = Depends(get_db)
):
    """Retrieve the current active shopping cart, including all items, line subtotals, and overall totals."""
    cart = crud.get_or_create_cart(db, cart_id=cart_id)
    return crud.format_cart_response(cart)


@router.post("/items", response_model=schemas.CartResponse, status_code=status.HTTP_201_CREATED, summary="Add item to cart")
def add_to_cart(
    item_in: schemas.CartItemCreate,
    cart_id: int = Query(1, ge=1, description="Cart ID"),
    db: Session = Depends(get_db)
):
    """Add a product to the cart with a specified quantity."""
    try:
        crud.add_item_to_cart(db, cart_id=cart_id, product_id=item_in.product_id, quantity=item_in.quantity)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    cart = crud.get_or_create_cart(db, cart_id=cart_id)
    return crud.format_cart_response(cart)


@router.put("/items/{item_id}", response_model=schemas.CartResponse, summary="Update cart item quantity")
def update_cart_item(
    item_id: int,
    item_in: schemas.CartItemUpdate,
    cart_id: int = Query(1, ge=1, description="Cart ID"),
    db: Session = Depends(get_db)
):
    """Update the quantity of an item in the cart. If quantity <= 0, the item is removed."""
    updated = crud.update_cart_item(db, item_id=item_id, quantity=item_in.quantity)
    if updated is None and item_in.quantity > 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cart item with ID {item_id} not found."
        )
    cart = crud.get_or_create_cart(db, cart_id=cart_id)
    return crud.format_cart_response(cart)


@router.delete("/items/{item_id}", response_model=schemas.CartResponse, summary="Remove item from cart")
def remove_from_cart(
    item_id: int,
    cart_id: int = Query(1, ge=1, description="Cart ID"),
    db: Session = Depends(get_db)
):
    """Remove a specific item from the shopping cart."""
    success = crud.remove_cart_item(db, item_id=item_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cart item with ID {item_id} not found."
        )
    cart = crud.get_or_create_cart(db, cart_id=cart_id)
    return crud.format_cart_response(cart)


@router.delete("", response_model=schemas.CartResponse, summary="Clear cart")
def clear_cart(
    cart_id: int = Query(1, ge=1, description="Cart ID"),
    db: Session = Depends(get_db)
):
    """Remove all items from the shopping cart."""
    crud.clear_cart(db, cart_id=cart_id)
    cart = crud.get_or_create_cart(db, cart_id=cart_id)
    return crud.format_cart_response(cart)
