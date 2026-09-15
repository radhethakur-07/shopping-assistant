from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("", response_model=List[schemas.ProductResponse], summary="Get all products")
def list_products(
    skip: int = Query(0, ge=0, description="Offset for pagination"),
    limit: int = Query(100, ge=1, le=200, description="Limit items returned"),
    category: Optional[str] = Query(None, description="Optional category filter"),
    db: Session = Depends(get_db)
):
    """Retrieve all available grocery products with optional category filtering and pagination."""
    return crud.get_products(db, skip=skip, limit=limit, category=category)


@router.get("/search", response_model=List[schemas.ProductResponse], summary="Search products")
def search_products(
    q: str = Query(..., min_length=1, description="Search term matching name, brand, category or description"),
    db: Session = Depends(get_db)
):
    """Search for products using a case-insensitive query string."""
    return crud.search_products(db, query_str=q)


@router.get("/category/{category}", response_model=List[schemas.ProductResponse], summary="Get products by category")
def get_products_by_category(
    category: str,
    db: Session = Depends(get_db)
):
    """Retrieve all products belonging to a specific category."""
    products = crud.get_products_by_category(db, category=category)
    return products


@router.get("/{id}", response_model=schemas.ProductResponse, summary="Get single product")
def get_product(
    id: int,
    db: Session = Depends(get_db)
):
    """Fetch details of a single product by its unique identifier."""
    product = crud.get_product(db, product_id=id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with ID {id} not found."
        )
    return product


@router.post("", response_model=schemas.ProductResponse, status_code=status.HTTP_201_CREATED, summary="Create new product")
def create_product(
    product_in: schemas.ProductCreate,
    db: Session = Depends(get_db)
):
    """Create and insert a new grocery product into the database."""
    return crud.create_product(db, product_in=product_in)


@router.put("/{id}", response_model=schemas.ProductResponse, summary="Update product")
def update_product(
    id: int,
    product_in: schemas.ProductUpdate,
    db: Session = Depends(get_db)
):
    """Update fields of an existing product."""
    updated = crud.update_product(db, product_id=id, product_in=product_in)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with ID {id} not found."
        )
    return updated


@router.delete("/{id}", status_code=status.HTTP_200_OK, summary="Delete product")
def delete_product(
    id: int,
    db: Session = Depends(get_db)
):
    """Delete a product from the database."""
    success = crud.delete_product(db, product_id=id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with ID {id} not found."
        )
    return {"status": "success", "message": f"Product {id} was successfully deleted."}
