"""
SmartCart Intelligent Grocery Recommendation Engine

This module implements an explainable multi-factor scoring recommendation system.
It evaluates:
1. Complementary Product Affinity (Frequently bought together graph)
2. Category Affinity & Cross-Selling Patterns
3. Customer Rating Weighting
4. Popularity & Stock Availability Score

Formula:
  RawScore = (w_comp * comp_score) + (w_cat * cat_score) + (w_rating * rating_score) + (w_pop * pop_score)
  NormalizedScore = min(1.0, max(0.1, RawScore / MaxPossibleScore))
"""

from typing import Dict, List, Optional, Set, Tuple
from sqlalchemy.orm import Session

from . import models, schemas


# =============================================================================
# Domain Knowledge Graph: Complementary & Frequently Bought Together Pairs
# Format: product keyword (lowercase) -> list of complementary product keywords
# =============================================================================
COMPLEMENTARY_RULES: Dict[str, List[str]] = {
    # Italian / Pasta
    "pasta": ["pasta sauce", "olive oil", "parmesan cheese", "oregano", "garlic", "cheese"],
    "spaghetti": ["pasta sauce", "olive oil", "parmesan cheese", "garlic", "cheese"],
    "pasta sauce": ["pasta", "spaghetti", "parmesan cheese", "olive oil", "oregano"],

    # Breakfast / Bakery
    "bread": ["butter", "fruit jam", "cheese", "eggs", "peanut butter", "milk", "tea"],
    "whole wheat bread": ["butter", "peanut butter", "eggs", "fruit jam", "cheese", "avocado"],
    "eggs": ["bread", "butter", "milk", "cheese", "cooking oil", "black pepper", "tomatoes"],
    "butter": ["bread", "fruit jam", "milk", "wheat flour", "sugar", "eggs"],
    "fruit jam": ["bread", "butter", "peanut butter", "biscuits"],
    "peanut butter": ["bread", "fruit jam", "oats", "bananas", "apples"],

    # Dairy / Morning
    "milk": ["breakfast cereal", "oats", "tea", "coffee", "cookies", "biscuits", "sugar", "bread"],
    "cheese": ["bread", "pasta", "crackers", "butter", "tomatoes", "tortilla chips"],
    "greek yogurt": ["honey", "apples", "bananas", "oats", "berries"],

    # Grains & Indian / Asian Staples
    "rice": ["yellow dal", "cooking oil", "turmeric powder", "onions", "tomatoes", "spices", "ghee"],
    "basmati rice": ["yellow dal", "cooking oil", "garam masala", "onions", "ghee"],
    "yellow dal": ["rice", "basmati rice", "turmeric powder", "cooking oil", "onions", "garlic", "salt"],
    "wheat flour": ["cooking oil", "butter", "salt", "sugar", "baking powder"],
    "oats": ["milk", "honey", "bananas", "apples", "peanut butter", "almonds"],

    # Beverages & Sweeteners
    "tea": ["milk", "sugar", "biscuits", "ginger", "cookies"],
    "green tea": ["honey", "lemon", "biscuits"],
    "coffee": ["milk", "sugar", "biscuits", "cookies", "dark chocolate"],
    "sugar": ["tea", "coffee", "wheat flour", "milk"],

    # Produce / Cooking Basics
    "tomatoes": ["onions", "potatoes", "garlic", "olive oil", "pasta sauce", "cooking oil", "salt"],
    "onions": ["potatoes", "tomatoes", "garlic", "cooking oil", "yellow dal", "rice"],
    "potatoes": ["onions", "cooking oil", "salt", "spices", "butter"],
    "apples": ["bananas", "peanut butter", "greek yogurt", "orange juice"],
    "bananas": ["apples", "oats", "milk", "peanut butter"],

    # Snacks & Party
    "tortilla chips": ["salsa", "cheese", "soda", "avocado"],
    "potato chips": ["soda", "cold drink", "cookies", "biscuits", "dip"],
    "biscuits": ["tea", "coffee", "milk"],
    "dark chocolate": ["coffee", "almonds", "green tea"],

    # Household & Personal Care
    "shampoo": ["conditioner", "body wash", "soap", "toothpaste", "hand sanitizer"],
    "soap": ["shampoo", "body wash", "toothpaste", "hand sanitizer"],
    "detergent": ["dish soap", "cleaning spray", "paper towels", "fabric softener"],
    "dish soap": ["detergent", "cleaning spray", "sponge"],
    "toothpaste": ["toothbrush", "shampoo", "soap", "mouthwash"],
}

# Category cross-sell affinity weights (Category A -> affinity with Category B)
CATEGORY_AFFINITY: Dict[str, List[str]] = {
    "Bakery": ["Dairy", "Beverages", "Snacks"],
    "Dairy": ["Bakery", "Beverages", "Grains"],
    "Grains": ["Vegetables", "Spices", "Dairy"],
    "Vegetables": ["Grains", "Fruits", "Dairy"],
    "Fruits": ["Dairy", "Beverages", "Snacks"],
    "Beverages": ["Snacks", "Bakery", "Dairy"],
    "Snacks": ["Beverages", "Dairy"],
    "Personal Care": ["Household"],
    "Household": ["Personal Care"],
    "Frozen Food": ["Beverages", "Snacks"],
}


def _normalize_name(name: str) -> str:
    return name.lower().strip()


def _get_target_keywords_for_item(item_name: str) -> List[str]:
    """Find matching complementary keywords from domain knowledge graph for a given item name."""
    norm = _normalize_name(item_name)
    targets = []
    for key, complements in COMPLEMENTARY_RULES.items():
        if key in norm or norm in key:
            targets.extend(complements)
    return list(set(targets))


def calculate_recommendations(
    db: Session,
    cart_id: Optional[int] = None,
    shopping_list_id: Optional[int] = None,
    limit: int = 8
) -> schemas.RecommendationResponse:
    """
    Generate scored, explainable product recommendations based on active cart or shopping list.
    """
    # 1. Gather all existing context items
    context_product_ids: Set[int] = set()
    cart_products: List[models.Product] = []
    list_products: List[models.Product] = []
    context_source = "popular"

    if cart_id:
        cart = db.query(models.Cart).filter(models.Cart.id == cart_id).first()
        if cart and cart.items:
            for ci in cart.items:
                if ci.product:
                    context_product_ids.add(ci.product_id)
                    cart_products.append(ci.product)
            if cart_products:
                context_source = "cart"

    if shopping_list_id:
        s_list = db.query(models.ShoppingList).filter(models.ShoppingList.id == shopping_list_id).first()
        if s_list and s_list.items:
            for sli in s_list.items:
                if sli.product:
                    context_product_ids.add(sli.product_id)
                    list_products.append(sli.product)
            if list_products:
                context_source = "shopping_list" if not cart_products else "combined"

    # Context categories and target keywords
    active_categories: Set[str] = set()
    for p in cart_products + list_products:
        active_categories.add(p.category)

    # 2. Fetch all candidate products from database (excluding already added products)
    all_products: List[models.Product] = db.query(models.Product).filter(
        models.Product.stock_quantity > 0
    ).all()

    candidates = [p for p in all_products if p.id not in context_product_ids]

    # If no candidates remain or no context exists, return top-rated popular items
    if not candidates:
        return schemas.RecommendationResponse(recommendations=[], total_count=0, context_source="empty")

    scored_candidates: List[Tuple[models.Product, float, str, str]] = []

    for candidate in candidates:
        candidate_norm_name = _normalize_name(candidate.name)
        comp_score = 0.0
        cat_score = 0.0
        reason = "Popular choice among shoppers"
        rec_type = "popular"

        # Check complementary matches from Cart
        matched_cart_source = None
        for cp in cart_products:
            targets = _get_target_keywords_for_item(cp.name)
            for tgt in targets:
                if tgt in candidate_norm_name or candidate_norm_name in tgt:
                    comp_score = max(comp_score, 0.95)
                    matched_cart_source = cp.name
                    reason = f"Frequently paired with '{matched_cart_source}' in your cart"
                    rec_type = "complementary"
                    break
            if comp_score >= 0.95:
                break

        # Check complementary matches from Shopping List if not already matched
        if comp_score < 0.95:
            for lp in list_products:
                targets = _get_target_keywords_for_item(lp.name)
                for tgt in targets:
                    if tgt in candidate_norm_name or candidate_norm_name in tgt:
                        comp_score = max(comp_score, 0.85)
                        reason = f"Complements '{lp.name}' in your shopping list"
                        rec_type = "complementary"
                        break
                if comp_score >= 0.85:
                    break

        # Category affinity scoring
        if candidate.category in active_categories:
            cat_score = 0.70
            if rec_type == "popular":
                reason = f"Popular top pick in {candidate.category}"
                rec_type = "category_affinity"
        else:
            # Check related cross-category affinity
            for act_cat in active_categories:
                affinities = CATEGORY_AFFINITY.get(act_cat, [])
                if candidate.category in affinities:
                    cat_score = max(cat_score, 0.50)
                    if rec_type == "popular":
                        reason = f"Pairs well with your {act_cat} selections"
                        rec_type = "category_affinity"
                    break

        # Rating score (0.0 to 1.0)
        rating_score = (candidate.rating / 5.0) if candidate.rating else 0.8

        # Popularity score based on stock & balanced pricing (0.0 to 1.0)
        pop_score = min(1.0, (candidate.stock_quantity / 100.0)) * 0.5 + 0.5

        # Weighted final composite score
        # Weights:
        # If complementary match exists: comp (0.50), cat (0.20), rating (0.20), pop (0.10)
        # If no context: rating (0.50), pop (0.30), cat (0.20)
        if comp_score > 0:
            raw_score = (comp_score * 0.50) + (cat_score * 0.20) + (rating_score * 0.20) + (pop_score * 0.10)
        elif cat_score > 0:
            raw_score = (cat_score * 0.45) + (rating_score * 0.35) + (pop_score * 0.20)
        else:
            raw_score = (rating_score * 0.60) + (pop_score * 0.40)
            if candidate.rating >= 4.7:
                reason = f"Top-rated grocery favorite ({candidate.rating} stars)"
            else:
                reason = f"Essential grocery staple in {candidate.category}"

        # Normalized final confidence score clamped between 0.50 and 0.99
        final_score = round(min(0.99, max(0.50, raw_score)), 2)

        scored_candidates.append((candidate, final_score, reason, rec_type))

    # Sort descending by computed score, then by rating
    scored_candidates.sort(key=lambda x: (x[1], x[0].rating), reverse=True)

    # Pick top N items
    top_items = scored_candidates[:limit]

    # Convert to response schemas
    recommendation_items = [
        schemas.RecommendationItem(
            product=schemas.ProductResponse.model_validate(prod),
            score=score,
            reason=reason_text,
            recommendation_type=r_type
        )
        for prod, score, reason_text, r_type in top_items
    ]

    return schemas.RecommendationResponse(
        recommendations=recommendation_items,
        total_count=len(recommendation_items),
        context_source=context_source
    )
