from typing import Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from .. import recommendations, schemas
from ..database import get_db

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"]
)


@router.get("", response_model=schemas.RecommendationResponse, summary="Get smart grocery recommendations")
def get_recommendations(
    cart_id: Optional[int] = Query(None, description="Optional cart ID to base recommendations on"),
    shopping_list_id: Optional[int] = Query(None, description="Optional shopping list ID to base recommendations on"),
    limit: int = Query(8, ge=1, le=20, description="Maximum number of recommendations to return"),
    db: Session = Depends(get_db)
):
    """
    Generate contextual, explainable grocery product recommendations.
    
    If cart_id or shopping_list_id is provided, the algorithm analyzes the contents
    to identify complementary pairings, category affinities, and popular co-occurrences.
    """
    return recommendations.calculate_recommendations(
        db=db,
        cart_id=cart_id,
        shopping_list_id=shopping_list_id,
        limit=limit
    )
