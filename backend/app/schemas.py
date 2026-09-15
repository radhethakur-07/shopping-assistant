from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field


# -----------------------------------------------------------------------------
# Product Schemas
# -----------------------------------------------------------------------------
class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255, description="Product name")
    description: Optional[str] = Field(None, description="Detailed product description")
    category: str = Field(..., min_length=1, max_length=100, description="Product category")
    brand: Optional[str] = Field(None, max_length=100, description="Brand name")
    price: float = Field(..., gt=0, description="Price per unit in standard currency")
    unit: str = Field("1 unit", max_length=50, description="Unit measurement, e.g., 1 kg, 500 ml, 1 pack")
    image_url: Optional[str] = Field(None, description="Public image URL")
    stock_quantity: int = Field(50, ge=0, description="Available stock quantity")
    rating: float = Field(4.5, ge=0.0, le=5.0, description="Average customer rating from 0.0 to 5.0")


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    category: Optional[str] = Field(None, min_length=1, max_length=100)
    brand: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)
    unit: Optional[str] = None
    image_url: Optional[str] = None
    stock_quantity: Optional[int] = Field(None, ge=0)
    rating: Optional[float] = Field(None, ge=0.0, le=5.0)


class ProductResponse(ProductBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# -----------------------------------------------------------------------------
# Cart Schemas
# -----------------------------------------------------------------------------
class CartItemBase(BaseModel):
    product_id: int = Field(..., description="ID of the product to add")
    quantity: int = Field(1, ge=1, description="Quantity to purchase (must be at least 1)")


class CartItemCreate(CartItemBase):
    pass


class CartItemUpdate(BaseModel):
    quantity: int = Field(..., ge=1, description="Updated quantity")


class CartItemResponse(BaseModel):
    id: int
    cart_id: int
    product_id: int
    quantity: int
    product: ProductResponse
    subtotal: float

    model_config = ConfigDict(from_attributes=True)


class CartResponse(BaseModel):
    id: int
    created_at: datetime
    items: List[CartItemResponse] = []
    item_count: int = 0
    total_quantity: int = 0
    subtotal: float = 0.0
    tax: float = 0.0
    total_price: float = 0.0

    model_config = ConfigDict(from_attributes=True)


# -----------------------------------------------------------------------------
# Shopping List Schemas
# -----------------------------------------------------------------------------
class ShoppingListItemCreate(BaseModel):
    product_id: int = Field(..., description="Product ID to add to shopping list")
    quantity: int = Field(1, ge=1, description="Quantity desired")


class ShoppingListItemUpdate(BaseModel):
    quantity: Optional[int] = Field(None, ge=1)
    purchased: Optional[bool] = None


class ShoppingListItemPurchasedUpdate(BaseModel):
    purchased: bool = Field(..., description="Mark item as purchased (true) or unpurchased (false)")


class ShoppingListItemResponse(BaseModel):
    id: int
    shopping_list_id: int
    product_id: int
    quantity: int
    purchased: bool
    product: ProductResponse

    model_config = ConfigDict(from_attributes=True)


class ShoppingListResponse(BaseModel):
    id: int
    name: str
    created_at: datetime
    items: List[ShoppingListItemResponse] = []
    total_items: int = 0
    purchased_items: int = 0
    pending_items: int = 0
    completion_percentage: float = 0.0

    model_config = ConfigDict(from_attributes=True)


# -----------------------------------------------------------------------------
# Recommendation Schemas
# -----------------------------------------------------------------------------
class RecommendationItem(BaseModel):
    product: ProductResponse
    score: float = Field(..., description="Computed recommendation confidence score (0.0 - 1.0)")
    reason: str = Field(..., description="Explainable reason for the recommendation")
    recommendation_type: str = Field(..., description="Type of recommendation (complementary, category_affinity, popular, trending)")

    model_config = ConfigDict(from_attributes=True)


class RecommendationResponse(BaseModel):
    recommendations: List[RecommendationItem] = []
    total_count: int = 0
    context_source: str = Field(..., description="Source context used (cart, shopping_list, popular, or combined)")
