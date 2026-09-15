from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(
    prefix="/shopping-list",
    tags=["Shopping List"]
)


@router.get("", response_model=schemas.ShoppingListResponse, summary="Get shopping list")
def get_shopping_list(
    list_id: int = Query(1, ge=1, description="Shopping List ID"),
    db: Session = Depends(get_db)
):
    """Retrieve the current shopping list, including all items and completion statistics."""
    s_list = crud.get_or_create_shopping_list(db, list_id=list_id)
    return crud.format_shopping_list_response(s_list)


@router.post("/items", response_model=schemas.ShoppingListResponse, status_code=status.HTTP_201_CREATED, summary="Add item to shopping list")
def add_to_shopping_list(
    item_in: schemas.ShoppingListItemCreate,
    list_id: int = Query(1, ge=1, description="Shopping List ID"),
    db: Session = Depends(get_db)
):
    """Add a product to the shopping list with desired quantity."""
    try:
        crud.add_item_to_shopping_list(db, list_id=list_id, product_id=item_in.product_id, quantity=item_in.quantity)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    s_list = crud.get_or_create_shopping_list(db, list_id=list_id)
    return crud.format_shopping_list_response(s_list)


@router.put("/items/{item_id}", response_model=schemas.ShoppingListResponse, summary="Update shopping list item")
def update_shopping_list_item(
    item_id: int,
    item_in: schemas.ShoppingListItemUpdate,
    list_id: int = Query(1, ge=1, description="Shopping List ID"),
    db: Session = Depends(get_db)
):
    """Update item quantity or purchased state in the shopping list."""
    updated = crud.update_shopping_list_item(
        db,
        item_id=item_id,
        quantity=item_in.quantity,
        purchased=item_in.purchased
    )
    if not updated and item_in.quantity and item_in.quantity > 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Shopping list item with ID {item_id} not found."
        )
    s_list = crud.get_or_create_shopping_list(db, list_id=list_id)
    return crud.format_shopping_list_response(s_list)


@router.patch("/items/{item_id}/purchased", response_model=schemas.ShoppingListResponse, summary="Toggle purchased status")
def toggle_purchased(
    item_id: int,
    status_in: schemas.ShoppingListItemPurchasedUpdate,
    list_id: int = Query(1, ge=1, description="Shopping List ID"),
    db: Session = Depends(get_db)
):
    """Mark a shopping list item as purchased or unpurchased."""
    updated = crud.toggle_shopping_list_item_purchased(db, item_id=item_id, purchased=status_in.purchased)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Shopping list item with ID {item_id} not found."
        )
    s_list = crud.get_or_create_shopping_list(db, list_id=list_id)
    return crud.format_shopping_list_response(s_list)


@router.delete("/items/{item_id}", response_model=schemas.ShoppingListResponse, summary="Remove item from shopping list")
def remove_from_shopping_list(
    item_id: int,
    list_id: int = Query(1, ge=1, description="Shopping List ID"),
    db: Session = Depends(get_db)
):
    """Remove a specific item from the shopping list."""
    success = crud.remove_shopping_list_item(db, item_id=item_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Shopping list item with ID {item_id} not found."
        )
    s_list = crud.get_or_create_shopping_list(db, list_id=list_id)
    return crud.format_shopping_list_response(s_list)


@router.delete("", response_model=schemas.ShoppingListResponse, summary="Clear shopping list")
def clear_shopping_list(
    list_id: int = Query(1, ge=1, description="Shopping List ID"),
    db: Session = Depends(get_db)
):
    """Remove all items from the shopping list."""
    crud.clear_shopping_list(db, list_id=list_id)
    s_list = crud.get_or_create_shopping_list(db, list_id=list_id)
    return crud.format_shopping_list_response(s_list)
