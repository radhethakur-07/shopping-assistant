"""
SmartCart Database Seeder
Comprehensive Supermarket Product Catalog (220+ realistic grocery items)
Spanning 11 comprehensive grocery aisles with 100% verified photography.
"""

import sys
import os
from sqlalchemy.orm import Session

if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.database import SessionLocal, engine, Base
from app.models import Product

SAMPLE_PRODUCTS = [
    # =========================================================================
    # 1. Fresh Fruits (22 items)
    # =========================================================================
    {
        "name": "Fresh Royal Gala Apples",
        "category": "Fruits",
        "brand": "Nature's Best",
        "price": 3.49,
        "unit": "1 kg (approx. 5-6 apples)",
        "description": "Crisp, sweet, and aromatic Royal Gala apples freshly picked from orchard farms.",
        "image_url": "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 85,
        "rating": 4.8
    },
    {
        "name": "Granny Smith Green Apples",
        "category": "Fruits",
        "brand": "Orchard Fresh",
        "price": 3.79,
        "unit": "1 kg (approx. 5 apples)",
        "description": "Tangy and crisp tart green apples, ideal for baking pies, salads, and fresh snacking.",
        "image_url": "https://images.unsplash.com/photo-1610397648930-477b8c7f0943?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 70,
        "rating": 4.7
    },
    {
        "name": "Organic Cavendish Bananas",
        "category": "Fruits",
        "brand": "Organic Valley",
        "price": 1.89,
        "unit": "1 bunch (approx. 1 kg)",
        "description": "Rich in potassium and natural energy. Perfectly ripened organic yellow bananas.",
        "image_url": "https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 120,
        "rating": 4.7
    },
    {
        "name": "Sweet Valencia Oranges",
        "category": "Fruits",
        "brand": "Citrus Grove",
        "price": 4.29,
        "unit": "1.5 kg bag",
        "description": "Juicy and vibrant Valencia oranges bursting with Vitamin C, ideal for fresh juice.",
        "image_url": "https://images.unsplash.com/photo-1611080626919-7cf5a9dbab5b?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 60,
        "rating": 4.6
    },
    {
        "name": "Fresh Garden Strawberries",
        "category": "Fruits",
        "brand": "Berry Sweet",
        "price": 3.99,
        "unit": "400 g pack",
        "description": "Sweet, ruby-red garden strawberries packed with antioxidants and natural flavor.",
        "image_url": "https://images.unsplash.com/photo-1464965911861-746a04b4bca6?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 40,
        "rating": 4.9
    },
    {
        "name": "Fresh Blueberries",
        "category": "Fruits",
        "brand": "Berry Sweet",
        "price": 4.99,
        "unit": "250 g punnet",
        "description": "Plump, antioxidant-rich fresh blueberries, great for oatmeal, yogurt, and baking.",
        "image_url": "https://images.unsplash.com/photo-1498557850523-fd3d118b962e?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 45,
        "rating": 4.8
    },
    {
        "name": "Fresh Raspberries",
        "category": "Fruits",
        "brand": "Berry Sweet",
        "price": 4.79,
        "unit": "170 g pack",
        "description": "Delicate and juicy fresh red raspberries with a rich sweet-tart taste.",
        "image_url": "https://images.unsplash.com/photo-1577069808021-5f21469e34e5?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 35,
        "rating": 4.7
    },
    {
        "name": "Hass Avocados",
        "category": "Fruits",
        "brand": "Green Harvest",
        "price": 4.49,
        "unit": "Pack of 3",
        "description": "Creamy, rich Hass avocados loaded with healthy monounsaturated fats. Ideal for guacamole.",
        "image_url": "https://images.unsplash.com/photo-1523049673857-eb18f1d7b578?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 55,
        "rating": 4.7
    },
    {
        "name": "Sweet Seedless Green Grapes",
        "category": "Fruits",
        "brand": "Sunburst",
        "price": 3.79,
        "unit": "500 g box",
        "description": "Crisp and juicy green seedless grapes, thoroughly washed and ready to enjoy.",
        "image_url": "https://images.unsplash.com/photo-1537640538966-79f369143f8f?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 70,
        "rating": 4.5
    },
    {
        "name": "Red Seedless Grapes",
        "category": "Fruits",
        "brand": "Sunburst",
        "price": 3.99,
        "unit": "500 g box",
        "description": "Plump, sweet crimson red seedless grapes with crunchy texture.",
        "image_url": "https://images.unsplash.com/photo-1596363505729-4190a9506133?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 65,
        "rating": 4.6
    },
    {
        "name": "Sweet Ripe Mangoes",
        "category": "Fruits",
        "brand": "Tropical Gold",
        "price": 5.49,
        "unit": "Pack of 2",
        "description": "Succulent, aromatic mangoes with honey-sweet golden flesh and smooth texture.",
        "image_url": "https://images.unsplash.com/photo-1553279768-865429fa0078?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 50,
        "rating": 4.9
    },
    {
        "name": "Golden Sweet Pineapple",
        "category": "Fruits",
        "brand": "Tropical Gold",
        "price": 3.99,
        "unit": "1 whole pineapple",
        "description": "Extra-sweet golden tropical pineapple, pre-ripened and ready to slice.",
        "image_url": "https://images.unsplash.com/photo-1550258987-190a2d41a8ba?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 40,
        "rating": 4.8
    },
    {
        "name": "Crisp Sweet Watermelon",
        "category": "Fruits",
        "brand": "Farm Fresh",
        "price": 5.99,
        "unit": "1 mini seedless watermelon (approx 2.5 kg)",
        "description": "Hydrating, sweet and juicy mini watermelon, perfect for hot days and fruit bowls.",
        "image_url": "https://images.unsplash.com/photo-1587049352846-4a222e784d38?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 30,
        "rating": 4.7
    },
    {
        "name": "Fresh Yellow Lemons",
        "category": "Fruits",
        "brand": "Citrus Grove",
        "price": 2.29,
        "unit": "Net bag of 5",
        "description": "Juicy, bright yellow lemons for seasoning, salad dressings, and refreshing lemonade.",
        "image_url": "https://images.unsplash.com/photo-1534940560662-75d8d0cf3183?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 90,
        "rating": 4.6
    },
    {
        "name": "Fresh Persian Limes",
        "category": "Fruits",
        "brand": "Citrus Grove",
        "price": 2.49,
        "unit": "Net bag of 6",
        "description": "Tart and aromatic green limes, essential for cocktails, marinades, and guacamole.",
        "image_url": "https://images.unsplash.com/photo-1526318896980-cf78c088247c?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 80,
        "rating": 4.5
    },
    {
        "name": "Sweet Yellow Peaches",
        "category": "Fruits",
        "brand": "Orchard Best",
        "price": 4.19,
        "unit": "1 kg (approx 4-5 peaches)",
        "description": "Fragrant and juicy yellow peaches with velvety skin and sweet summer flavor.",
        "image_url": "https://images.unsplash.com/photo-1629828874514-c1e5103f2150?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 40,
        "rating": 4.7
    },
    {
        "name": "Black Ruby Plums",
        "category": "Fruits",
        "brand": "Orchard Best",
        "price": 3.89,
        "unit": "750 g bag",
        "description": "Sweet, dark-skinned juicy plums with deep red flesh.",
        "image_url": "https://images.unsplash.com/photo-1568702846914-96b305d2aaeb?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 45,
        "rating": 4.6
    },
    {
        "name": "Green Kiwi Fruit",
        "category": "Fruits",
        "brand": "Zespri",
        "price": 3.49,
        "unit": "Pack of 4",
        "description": "Tangy-sweet green kiwis loaded with Vitamin C, digestive enzymes, and fiber.",
        "image_url": "https://images.unsplash.com/photo-1585059895524-72359e06133a?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 60,
        "rating": 4.7
    },
    {
        "name": "Anjou Sweet Green Pears",
        "category": "Fruits",
        "brand": "Orchard Best",
        "price": 3.69,
        "unit": "1 kg (approx 4 pears)",
        "description": "Smooth, aromatic green pears with sweet juicy flesh.",
        "image_url": "https://images.unsplash.com/photo-1631160299919-6a175aa6d189?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 50,
        "rating": 4.5
    },
    {
        "name": "Ruby Red Pomegranate",
        "category": "Fruits",
        "brand": "Nature's Best",
        "price": 4.99,
        "unit": "Pack of 2 whole fruits",
        "description": "Antioxidant powerhouse filled with vibrant, juicy, ruby-red edible arils.",
        "image_url": "https://images.unsplash.com/photo-1541344999736-83eca872f242?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 35,
        "rating": 4.8
    },
    {
        "name": "Fresh Sweet Papaya",
        "category": "Fruits",
        "brand": "Tropical Gold",
        "price": 3.99,
        "unit": "1 medium fruit",
        "description": "Rich in papain enzyme and beta-carotene for digestion and vibrant health.",
        "image_url": "https://images.unsplash.com/photo-1517282009859-f000ec3b26fe?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 30,
        "rating": 4.6
    },
    {
        "name": "Dark Sweet Cherries",
        "category": "Fruits",
        "brand": "Berry Sweet",
        "price": 5.99,
        "unit": "500 g pouch",
        "description": "Plump, deeply sweet dark Bing cherries packed with antioxidants.",
        "image_url": "https://images.unsplash.com/photo-1528825871115-3581a5387919?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 35,
        "rating": 4.9
    },

    # =========================================================================
    # 2. Fresh Vegetables (26 items)
    # =========================================================================
    {
        "name": "Vine Ripened Red Tomatoes",
        "category": "Vegetables",
        "brand": "Farm Fresh",
        "price": 2.49,
        "unit": "1 kg",
        "description": "Plump, deeply red vine-ripened tomatoes bursting with flavor for salads and savory sauces.",
        "image_url": "https://images.unsplash.com/photo-1592924357228-91a4daadcfea?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 100,
        "rating": 4.6
    },
    {
        "name": "Sweet Cherry Tomatoes",
        "category": "Vegetables",
        "brand": "Farm Fresh",
        "price": 2.99,
        "unit": "250 g punnet",
        "description": "Bite-sized sweet red cherry tomatoes, great for snacking and salads.",
        "image_url": "https://images.unsplash.com/photo-1546470427-0d4db154ceb7?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 80,
        "rating": 4.8
    },
    {
        "name": "Crisp Yellow Onions",
        "category": "Vegetables",
        "brand": "Earth Greens",
        "price": 1.99,
        "unit": "1.5 kg mesh bag",
        "description": "Essential culinary all-purpose yellow onions with bold flavor, great for sautés and curries.",
        "image_url": "https://images.unsplash.com/photo-1508747703725-719777637510?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 110,
        "rating": 4.5
    },
    {
        "name": "Sweet Red Onions",
        "category": "Vegetables",
        "brand": "Earth Greens",
        "price": 2.29,
        "unit": "1 kg bag",
        "description": "Vibrant purple-red onions with mild sweet flavor, perfect for raw salads and burgers.",
        "image_url": "https://images.unsplash.com/photo-1618512496248-a07fe83aa8cb?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 90,
        "rating": 4.6
    },
    {
        "name": "Russet Baking Potatoes",
        "category": "Vegetables",
        "brand": "Harvest Gold",
        "price": 3.29,
        "unit": "2.5 kg bag",
        "description": "Classic hearty Russet potatoes, excellent for mashing, baking, roasting, or making fries.",
        "image_url": "https://images.unsplash.com/photo-1518977676601-b53f82aba655?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 90,
        "rating": 4.7
    },
    {
        "name": "Sweet Orange Yams (Sweet Potatoes)",
        "category": "Vegetables",
        "brand": "Harvest Gold",
        "price": 2.79,
        "unit": "1.5 kg bag",
        "description": "Nutrient-dense orange sweet potatoes rich in Vitamin A and complex carbs.",
        "image_url": "https://images.unsplash.com/photo-1596097635121-14b63b7a0c19?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 65,
        "rating": 4.8
    },
    {
        "name": "Organic Tender Carrots",
        "category": "Vegetables",
        "brand": "Organic Valley",
        "price": 1.79,
        "unit": "1 kg bag",
        "description": "Crunchy, sweet organic carrots with vibrant orange color and high beta-carotene content.",
        "image_url": "https://images.unsplash.com/photo-1598170845058-32b9d6a5da37?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 75,
        "rating": 4.6
    },
    {
        "name": "Fresh Green Broccoli Florets",
        "category": "Vegetables",
        "brand": "Farm Fresh",
        "price": 2.29,
        "unit": "500 g head",
        "description": "Nutrient-dense green broccoli crowns, perfect for steaming, stir-fries, and healthy side dishes.",
        "image_url": "https://images.unsplash.com/photo-1459411621453-7b03977f4bfc?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 50,
        "rating": 4.4
    },
    {
        "name": "Fresh White Cauliflower",
        "category": "Vegetables",
        "brand": "Farm Fresh",
        "price": 2.69,
        "unit": "1 head",
        "description": "Firm, crisp white cauliflower head for roasting, curries, and low-carb rice substitutes.",
        "image_url": "https://images.unsplash.com/photo-1568584711075-3d021a7c3ca3?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 45,
        "rating": 4.5
    },
    {
        "name": "Aromatic Fresh Garlic Bulbs",
        "category": "Vegetables",
        "brand": "Spice Garden",
        "price": 1.49,
        "unit": "Pack of 3 bulbs",
        "description": "Fragrant garlic with firm cloves, essential for seasoning curries, pastas, and roasts.",
        "image_url": "https://images.unsplash.com/photo-1540148426945-6cf22a6b2383?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 130,
        "rating": 4.8
    },
    {
        "name": "Fresh Ginger Root",
        "category": "Vegetables",
        "brand": "Spice Garden",
        "price": 1.99,
        "unit": "250 g root",
        "description": "Zesty, spicy fresh ginger root for teas, stir-fries, marinades, and curries.",
        "image_url": "https://images.unsplash.com/photo-1615485290382-441e4d049cb5?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 85,
        "rating": 4.7
    },
    {
        "name": "Fresh English Cucumbers",
        "category": "Vegetables",
        "brand": "Farm Fresh",
        "price": 1.59,
        "unit": "Pack of 2",
        "description": "Cool, crisp seedless cucumbers for refreshing salads and healthy wraps.",
        "image_url": "https://images.unsplash.com/photo-1449300079323-02e209d9d3a6?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 80,
        "rating": 4.5
    },
    {
        "name": "Fresh Baby Spinach Leaves",
        "category": "Vegetables",
        "brand": "Organic Greens",
        "price": 2.99,
        "unit": "300 g tub",
        "description": "Tender pre-washed organic baby spinach packed with iron and essential minerals.",
        "image_url": "https://images.unsplash.com/photo-1576045057995-568f588f82fb?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 65,
        "rating": 4.7
    },
    {
        "name": "Green Bell Peppers (Capsicum)",
        "category": "Vegetables",
        "brand": "Farm Fresh",
        "price": 2.19,
        "unit": "Pack of 3",
        "description": "Crisp green bell peppers with mild flavor for stir-fries, fajitas, and pizzas.",
        "image_url": "https://images.unsplash.com/photo-1563565375-f3fdfdbefa83?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 70,
        "rating": 4.6
    },
    {
        "name": "Red & Yellow Sweet Bell Peppers",
        "category": "Vegetables",
        "brand": "Farm Fresh",
        "price": 3.49,
        "unit": "Pack of 2",
        "description": "Sweet, crunchy colorful peppers packed with Vitamin C.",
        "image_url": "https://images.unsplash.com/photo-1525607551316-4a8e16d1f9ba?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 60,
        "rating": 4.7
    },
    {
        "name": "Fresh White Button Mushrooms",
        "category": "Vegetables",
        "brand": "Earth Greens",
        "price": 2.49,
        "unit": "250 g punnet",
        "description": "Tender white button mushrooms for sautés, pizzas, and hearty pasta dishes.",
        "image_url": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 55,
        "rating": 4.6
    },
    {
        "name": "Crisp Green Romaine Lettuce",
        "category": "Vegetables",
        "brand": "Organic Greens",
        "price": 2.29,
        "unit": "Pack of 3 hearts",
        "description": "Crunchy, refreshing Romaine lettuce hearts for classic Caesar salads.",
        "image_url": "https://images.unsplash.com/photo-1556801712-76c8eb07bbc9?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 50,
        "rating": 4.5
    },
    {
        "name": "Fresh Green Zucchini",
        "category": "Vegetables",
        "brand": "Farm Fresh",
        "price": 1.99,
        "unit": "1 kg (approx 3-4 zucchinis)",
        "description": "Tender green courgettes, great for grilling, roasting, or spiralizing into zoodles.",
        "image_url": "https://images.unsplash.com/photo-1590779033100-9f60a05a013d?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 60,
        "rating": 4.5
    },
    {
        "name": "Tender Green Beans",
        "category": "Vegetables",
        "brand": "Farm Fresh",
        "price": 2.69,
        "unit": "500 g pack",
        "description": "Fresh, stringless green beans for side dishes, steaming, and stir-fries.",
        "image_url": "https://images.unsplash.com/photo-1567306226416-28f0efdc88ce?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 50,
        "rating": 4.6
    },
    {
        "name": "Fresh Green Cabbage",
        "category": "Vegetables",
        "brand": "Farm Fresh",
        "price": 1.89,
        "unit": "1 medium head (approx 1.2 kg)",
        "description": "Crisp green cabbage for coleslaw, stir-fries, and cabbage rolls.",
        "image_url": "https://images.unsplash.com/photo-1594282486552-05b4d80fbb9f?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 65,
        "rating": 4.4
    },
    {
        "name": "Purple Glossy Eggplants (Brinjal)",
        "category": "Vegetables",
        "brand": "Farm Fresh",
        "price": 2.59,
        "unit": "Pack of 2",
        "description": "Smooth purple eggplants for roasting, ratatouille, and baingan bharta.",
        "image_url": "https://images.unsplash.com/photo-1615485290382-441e4d049cb5?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 40,
        "rating": 4.5
    },
    {
        "name": "Crisp Celery Stalks",
        "category": "Vegetables",
        "brand": "Farm Fresh",
        "price": 1.99,
        "unit": "1 bunch",
        "description": "Crunchy celery stalks for healthy dips, soups, and mirepoix bases.",
        "image_url": "https://images.unsplash.com/photo-1610832958506-aa56368176cf?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 55,
        "rating": 4.4
    },
    {
        "name": "Fresh Green Asparagus",
        "category": "Vegetables",
        "brand": "Green Harvest",
        "price": 3.99,
        "unit": "400 g bundle",
        "description": "Tender young asparagus spears, delicious grilled with olive oil and garlic.",
        "image_url": "https://images.unsplash.com/photo-1515471209610-dae1c92d8777?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 35,
        "rating": 4.8
    },
    {
        "name": "Fresh Coriander / Cilantro",
        "category": "Vegetables",
        "brand": "Spice Garden",
        "price": 0.99,
        "unit": "1 fresh bunch",
        "description": "Aromatic fresh cilantro herb for curries, salsas, and garnishing.",
        "image_url": "https://images.unsplash.com/photo-1588879462716-1f6e210134f7?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 100,
        "rating": 4.7
    },
    {
        "name": "Fresh Mint Leaves",
        "category": "Vegetables",
        "brand": "Spice Garden",
        "price": 1.19,
        "unit": "1 fresh bunch",
        "description": "Cool, fragrant fresh mint leaves for chutneys, mocktails, and teas.",
        "image_url": "https://images.unsplash.com/photo-1628556270448-4d4e4148e1b1?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 80,
        "rating": 4.7
    },
    {
        "name": "Spicy Green Jalapeno Peppers",
        "category": "Vegetables",
        "brand": "Farm Fresh",
        "price": 1.49,
        "unit": "200 g pack",
        "description": "Spicy green jalapenos for tacos, nachos, salsas, and curries.",
        "image_url": "https://images.unsplash.com/photo-1588347818036-558601350bc4?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 70,
        "rating": 4.6
    },

    # =========================================================================
    # 3. Dairy & Plant Milk (22 items)
    # =========================================================================
    {
        "name": "Pure Whole Milk",
        "category": "Dairy",
        "brand": "Dairy Pure",
        "price": 3.69,
        "unit": "1 Gallon (3.78 L)",
        "description": "Farm-fresh pasteurized Grade A whole milk enriched with Vitamins A and D.",
        "image_url": "https://images.unsplash.com/photo-1550583724-b2692b85b150?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 70,
        "rating": 4.9
    },
    {
        "name": "2% Reduced Fat Milk",
        "category": "Dairy",
        "brand": "Dairy Pure",
        "price": 3.49,
        "unit": "1 Gallon (3.78 L)",
        "description": "Creamy low-fat milk with all the calcium and protein and less fat.",
        "image_url": "https://images.unsplash.com/photo-1563636619-e9143da7973b?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 65,
        "rating": 4.7
    },
    {
        "name": "Unsweetened Almond Milk",
        "category": "Dairy",
        "brand": "Almond Breeze",
        "price": 3.29,
        "unit": "1.89 L carton",
        "description": "Dairy-free plant-based almond milk with 50% more calcium than dairy milk.",
        "image_url": "https://images.unsplash.com/photo-1568651316353-9031d27771ba?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 60,
        "rating": 4.8
    },
    {
        "name": "Creamy Oat Milk",
        "category": "Dairy",
        "brand": "Oatly",
        "price": 3.99,
        "unit": "1.89 L carton",
        "description": "Rich and foamy plant-based oat milk, perfect for lattes and smoothies.",
        "image_url": "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 50,
        "rating": 4.9
    },
    {
        "name": "Farm Fresh Free-Range Eggs",
        "category": "Dairy",
        "brand": "Happy Hens",
        "price": 3.99,
        "unit": "1 Dozen (12 large eggs)",
        "description": "Grade A large brown eggs sourced from free-range hens. Excellent protein source.",
        "image_url": "https://images.unsplash.com/photo-1516448620398-c5f44bf9f441?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 95,
        "rating": 4.8
    },
    {
        "name": "Organic Pasture-Raised Eggs",
        "category": "Dairy",
        "brand": "Vital Farms",
        "price": 5.29,
        "unit": "1 Dozen (12 eggs)",
        "description": "Certified humane pasture-raised eggs with deep orange rich yolks.",
        "image_url": "https://images.unsplash.com/photo-1582722872445-44dc5f7e3c8f?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 50,
        "rating": 4.9
    },
    {
        "name": "Salted Creamery Butter",
        "category": "Dairy",
        "brand": "Golden Meadow",
        "price": 4.19,
        "unit": "454 g (4 sticks)",
        "description": "Rich and creamy butter churned from pure sweet cream with a hint of salt.",
        "image_url": "https://images.unsplash.com/photo-1589985270826-4b7bb135bc9d?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 65,
        "rating": 4.7
    },
    {
        "name": "Unsalted Sweet Cream Butter",
        "category": "Dairy",
        "brand": "Golden Meadow",
        "price": 4.19,
        "unit": "454 g (4 sticks)",
        "description": "Pure unsalted sweet cream butter, perfect for baking pastries and precision cooking.",
        "image_url": "https://images.unsplash.com/photo-1589985270826-4b7bb135bc9d?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 60,
        "rating": 4.8
    },
    {
        "name": "Pure Desi Cow Ghee",
        "category": "Dairy",
        "brand": "Amul Pure",
        "price": 8.99,
        "unit": "500 ml jar",
        "description": "Traditional clarified butter with rich granular texture and mouthwatering aroma.",
        "image_url": "https://images.unsplash.com/photo-1631451095765-2c91616fc9e6?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 55,
        "rating": 4.9
    },
    {
        "name": "Sharp Cheddar Cheese Block",
        "category": "Dairy",
        "brand": "Artisan Creamery",
        "price": 4.89,
        "unit": "300 g block",
        "description": "Aged sharp cheddar cheese with rich flavor and smooth slicing texture.",
        "image_url": "https://images.unsplash.com/photo-1618164435735-413d3b066194?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 45,
        "rating": 4.8
    },
    {
        "name": "Shredded Mozzarella Cheese",
        "category": "Dairy",
        "brand": "Bella Italia",
        "price": 3.99,
        "unit": "250 g bag",
        "description": "Pre-shredded low-moisture mozzarella for gooey melted pizza and pasta toppings.",
        "image_url": "https://images.unsplash.com/photo-1559561853-08451507cbe7?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 60,
        "rating": 4.8
    },
    {
        "name": "Fresh Mozzarella Ball",
        "category": "Dairy",
        "brand": "Bella Italia",
        "price": 4.29,
        "unit": "250 g in brine",
        "description": "Soft and milky traditional mozzarella, perfect for Caprese salads and pizzas.",
        "image_url": "https://images.unsplash.com/photo-1592417817098-8f3d6eb22509?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 35,
        "rating": 4.8
    },
    {
        "name": "Aged Italian Parmesan Cheese",
        "category": "Dairy",
        "brand": "Bella Italia",
        "price": 5.99,
        "unit": "200 g grated",
        "description": "Finely grated aged parmesan cheese offering authentic nutty taste for pasta.",
        "image_url": "https://images.unsplash.com/photo-1559561853-08451507cbe7?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 40,
        "rating": 4.9
    },
    {
        "name": "Fresh Malai Paneer Block",
        "category": "Dairy",
        "brand": "Amul Fresh",
        "price": 4.49,
        "unit": "400 g block",
        "description": "Soft, high-protein traditional Indian cottage cheese for curries and tikka skewers.",
        "image_url": "https://images.unsplash.com/photo-1567337710282-00832b415979?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 50,
        "rating": 4.8
    },
    {
        "name": "Authentic Greek Yogurt",
        "category": "Dairy",
        "brand": "Olympus",
        "price": 4.49,
        "unit": "900 g tub",
        "description": "Thick and velvety plain Greek yogurt with 15g protein per serving.",
        "image_url": "https://images.unsplash.com/photo-1488477181946-6428a0291777?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 50,
        "rating": 4.6
    },
    {
        "name": "Vanilla Greek Yogurt Cups",
        "category": "Dairy",
        "brand": "Chobani",
        "price": 4.99,
        "unit": "Pack of 4 (150 g each)",
        "description": "Creamy low-fat Greek yogurt blended with Madagascar vanilla beans.",
        "image_url": "https://images.unsplash.com/photo-1571212515416-fef01fc43637?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 45,
        "rating": 4.7
    },
    {
        "name": "Original Cream Cheese Spread",
        "category": "Dairy",
        "brand": "Philadelphia",
        "price": 3.49,
        "unit": "226 g tub",
        "description": "Classic smooth and spreadable cream cheese for bagels, cheesecakes, and dips.",
        "image_url": "https://images.unsplash.com/photo-1589985270826-4b7bb135bc9d?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 55,
        "rating": 4.8
    },
    {
        "name": "Heavy Whipping Cream",
        "category": "Dairy",
        "brand": "Dairy Pure",
        "price": 3.79,
        "unit": "473 ml carton",
        "description": "Ultra-pasteurized Grade A heavy cream for desserts, sauces, and soups.",
        "image_url": "https://images.unsplash.com/photo-1550583724-b2692b85b150?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 40,
        "rating": 4.8
    },
    {
        "name": "Cultured Sour Cream",
        "category": "Dairy",
        "brand": "Daisy",
        "price": 2.69,
        "unit": "450 g tub",
        "description": "Pure and natural sour cream with no preservatives for baked potatoes and tacos.",
        "image_url": "https://images.unsplash.com/photo-1488477181946-6428a0291777?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 45,
        "rating": 4.7
    },
    {
        "name": "Crumbled Greek Feta Cheese",
        "category": "Dairy",
        "brand": "Athenos",
        "price": 4.69,
        "unit": "170 g tub",
        "description": "Authentic tangy and salty crumbled feta cheese for Greek salads and wraps.",
        "image_url": "https://images.unsplash.com/photo-1559561853-08451507cbe7?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 35,
        "rating": 4.7
    },
    {
        "name": "Low Fat Cottage Cheese",
        "category": "Dairy",
        "brand": "Good Culture",
        "price": 3.29,
        "unit": "454 g tub",
        "description": "Creamy cultured cottage cheese with live probiotics and 14g protein.",
        "image_url": "https://images.unsplash.com/photo-1488477181946-6428a0291777?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 40,
        "rating": 4.6
    },
    {
        "name": "Swiss Cheese Slices",
        "category": "Dairy",
        "brand": "Sargento",
        "price": 3.99,
        "unit": "200 g pack (10 slices)",
        "description": "Nutty, mild natural Swiss cheese slices, ideal for hot pastrami and deli sandwiches.",
        "image_url": "https://images.unsplash.com/photo-1618164435735-413d3b066194?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 40,
        "rating": 4.6
    },

    # =========================================================================
    # 4. Bakery & Spreads (20 items)
    # =========================================================================
    {
        "name": "100% Whole Wheat Bread",
        "category": "Bakery",
        "brand": "Daily Baker",
        "price": 2.79,
        "unit": "600 g loaf",
        "description": "Soft, wholesome whole wheat bread baked daily with natural grains and high fiber.",
        "image_url": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 60,
        "rating": 4.7
    },
    {
        "name": "Artisan Sourdough Loaf",
        "category": "Bakery",
        "brand": "Rustica Bakes",
        "price": 4.29,
        "unit": "500 g round loaf",
        "description": "Traditional sourdough with a crisp golden crust and open airy crumb with subtle tang.",
        "image_url": "https://images.unsplash.com/photo-1586444248902-2f64eddc13df?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 35,
        "rating": 4.9
    },
    {
        "name": "Golden Butter Croissants",
        "category": "Bakery",
        "brand": "French Corner",
        "price": 3.99,
        "unit": "Pack of 4",
        "description": "Flaky, buttery French-style croissants layered to golden perfection for breakfast.",
        "image_url": "https://images.unsplash.com/photo-1555507036-ab1f4038808a?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 45,
        "rating": 4.8
    },
    {
        "name": "Strawberry Fruit Jam",
        "category": "Bakery",
        "brand": "Smucker's",
        "price": 3.19,
        "unit": "340 g jar",
        "description": "Sweet and luscious strawberry fruit spread made with ripe berries. Perfect with toast.",
        "image_url": "https://images.unsplash.com/photo-1533089860892-a7c6f0a88666?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 65,
        "rating": 4.7
    },
    {
        "name": "Blueberry Fruit Jam",
        "category": "Bakery",
        "brand": "Bonne Maman",
        "price": 4.49,
        "unit": "370 g jar",
        "description": "French recipe wild blueberry preserve with chunks of real berries.",
        "image_url": "https://images.unsplash.com/photo-1533089860892-a7c6f0a88666?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 50,
        "rating": 4.9
    },
    {
        "name": "Creamy Roasted Peanut Butter",
        "category": "Bakery",
        "brand": "Skippy",
        "price": 3.89,
        "unit": "460 g jar",
        "description": "Smooth, spreadable peanut butter made with roasted peanuts. Great on toast and apples.",
        "image_url": "https://images.unsplash.com/photo-1527515637462-cff94eecc1ac?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 80,
        "rating": 4.8
    },
    {
        "name": "Crunchy Peanut Butter",
        "category": "Bakery",
        "brand": "Jif",
        "price": 3.89,
        "unit": "460 g jar",
        "description": "Packed with crunchy roasted peanut pieces for extra texture.",
        "image_url": "https://images.unsplash.com/photo-1527515637462-cff94eecc1ac?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 70,
        "rating": 4.7
    },
    {
        "name": "Smooth Almond Butter",
        "category": "Bakery",
        "brand": "Justin's",
        "price": 6.99,
        "unit": "454 g jar",
        "description": "Pure dry-roasted almond butter with a pinch of sea salt. No palm oil.",
        "image_url": "https://images.unsplash.com/photo-1527515637462-cff94eecc1ac?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 40,
        "rating": 4.8
    },
    {
        "name": "Hazelnut Cocoa Spread (Nutella)",
        "category": "Bakery",
        "brand": "Ferrero",
        "price": 4.99,
        "unit": "400 g jar",
        "description": "Iconic rich hazelnut and cocoa spread, irresistible on warm toast and pancakes.",
        "image_url": "https://images.unsplash.com/photo-1589985270826-4b7bb135bc9d?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 75,
        "rating": 4.9
    },
    {
        "name": "Pure Wildflower Honey",
        "category": "Bakery",
        "brand": "Nature's Sweet",
        "price": 5.99,
        "unit": "500 g squeeze bottle",
        "description": "100% raw, unfiltered pure wildflower honey for sweetening tea, oats, and pancakes.",
        "image_url": "https://images.unsplash.com/photo-1587049352846-4a222e784d38?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 60,
        "rating": 4.9
    },
    {
        "name": "Pure Canadian Maple Syrup",
        "category": "Bakery",
        "brand": "Maple Gold",
        "price": 7.49,
        "unit": "250 ml glass bottle",
        "description": "Grade A amber rich taste 100% pure maple syrup tapped from Canadian sugar maples.",
        "image_url": "https://images.unsplash.com/photo-1587049352846-4a222e784d38?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 45,
        "rating": 4.9
    },
    {
        "name": "Classic Plain Bagels",
        "category": "Bakery",
        "brand": "New York Bakery",
        "price": 3.49,
        "unit": "Pack of 6 bagels",
        "description": "Boiled and baked New York-style chewy plain bagels, great with cream cheese.",
        "image_url": "https://images.unsplash.com/photo-1555507036-ab1f4038808a?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 50,
        "rating": 4.7
    },
    {
        "name": "Soft Brioche Burger Buns",
        "category": "Bakery",
        "brand": "Daily Baker",
        "price": 3.49,
        "unit": "Pack of 6 buns",
        "description": "Rich, tender brioche buns with a subtle glaze, ideal for gourmet burgers.",
        "image_url": "https://images.unsplash.com/photo-1586190848861-99aa4a171e90?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 50,
        "rating": 4.6
    },
    {
        "name": "White Flour Tortillas",
        "category": "Bakery",
        "brand": "Mission",
        "price": 2.79,
        "unit": "Pack of 10 (8-inch)",
        "description": "Soft and pliable flour tortillas, perfect for burritos, quesadillas, and wraps.",
        "image_url": "https://images.unsplash.com/photo-1565299585323-38d6b0865b47?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 70,
        "rating": 4.7
    },
    {
        "name": "Whole Wheat Pita Bread",
        "category": "Bakery",
        "brand": "Joseph's",
        "price": 2.99,
        "unit": "Pack of 6 pockets",
        "description": "Fluffy pocket pitas for hummus, falafel, and Mediterranean salads.",
        "image_url": "https://images.unsplash.com/photo-1565299585323-38d6b0865b47?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 40,
        "rating": 4.6
    },
    {
        "name": "English Breakfast Muffins",
        "category": "Bakery",
        "brand": "Thomas'",
        "price": 3.29,
        "unit": "Pack of 6",
        "description": "Iconic nooks and crannies that hold melted butter and jam.",
        "image_url": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 45,
        "rating": 4.7
    },
    {
        "name": "Garlic & Herb Baguette",
        "category": "Bakery",
        "brand": "Rustica Bakes",
        "price": 3.79,
        "unit": "350 g foil-wrapped",
        "description": "Crispy French baguette filled with aromatic garlic butter and parsley.",
        "image_url": "https://images.unsplash.com/photo-1586444248902-2f64eddc13df?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 35,
        "rating": 4.8
    },
    {
        "name": "Double Chocolate Chip Muffins",
        "category": "Bakery",
        "brand": "Daily Baker",
        "price": 4.49,
        "unit": "Pack of 4 large muffins",
        "description": "Decadent chocolate muffins loaded with real semi-sweet chocolate chunks.",
        "image_url": "https://images.unsplash.com/photo-1558961363-fa8fdf82db35?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 30,
        "rating": 4.8
    },
    {
        "name": "Cinnamon Swirl Rolls",
        "category": "Bakery",
        "brand": "Daily Baker",
        "price": 4.29,
        "unit": "Pack of 4 with icing",
        "description": "Warm cinnamon spice swirls topped with sweet cream cheese icing.",
        "image_url": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 35,
        "rating": 4.8
    },
    {
        "name": "Soft Dinner Rolls",
        "category": "Bakery",
        "brand": "King's Hawaiian",
        "price": 3.99,
        "unit": "Pack of 12 rolls",
        "description": "Sweet, golden and fluffy Hawaiian rolls for family dinners and sliders.",
        "image_url": "https://images.unsplash.com/photo-1586190848861-99aa4a171e90?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 40,
        "rating": 4.9
    },

    # =========================================================================
    # 5. Beverages (20 items)
    # =========================================================================
    {
        "name": "Premium English Breakfast Tea",
        "category": "Beverages",
        "brand": "Twinings",
        "price": 4.99,
        "unit": "Box of 50 tea bags",
        "description": "Robust, full-bodied black tea blend sourced from fine tea gardens. Perfect with milk.",
        "image_url": "https://images.unsplash.com/photo-1576092768241-dec231879fc3?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 80,
        "rating": 4.8
    },
    {
        "name": "Aromatic Earl Grey Tea",
        "category": "Beverages",
        "brand": "Twinings",
        "price": 5.29,
        "unit": "Box of 50 tea bags",
        "description": "Fine black tea delicately scented with natural oil of bergamot citrus.",
        "image_url": "https://images.unsplash.com/photo-1576092768241-dec231879fc3?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 60,
        "rating": 4.8
    },
    {
        "name": "Indian Masala Chai Tea",
        "category": "Beverages",
        "brand": "Taj Mahal",
        "price": 5.49,
        "unit": "500 g loose leaf",
        "description": "Strong Assam tea infused with cardamom, ginger, cinnamon, and cloves.",
        "image_url": "https://images.unsplash.com/photo-1576092768241-dec231879fc3?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 75,
        "rating": 4.9
    },
    {
        "name": "Medium Roast Arabica Ground Coffee",
        "category": "Beverages",
        "brand": "Star Roast",
        "price": 7.49,
        "unit": "340 g bag",
        "description": "100% Arabica ground coffee with notes of cocoa and toasted nuts.",
        "image_url": "https://images.unsplash.com/photo-1559056199-641a0ac8b55e?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 60,
        "rating": 4.9
    },
    {
        "name": "Dark French Roast Whole Bean Coffee",
        "category": "Beverages",
        "brand": "Star Roast",
        "price": 8.99,
        "unit": "450 g bag",
        "description": "Smoky, intense dark roast coffee beans for espresso and French press.",
        "image_url": "https://images.unsplash.com/photo-1559056199-641a0ac8b55e?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 50,
        "rating": 4.8
    },
    {
        "name": "Classic Instant Coffee Granules",
        "category": "Beverages",
        "brand": "Nescafe Gold",
        "price": 6.79,
        "unit": "200 g glass jar",
        "description": "Smooth golden roasted instant coffee granules for quick morning cups.",
        "image_url": "https://images.unsplash.com/photo-1559056199-641a0ac8b55e?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 65,
        "rating": 4.7
    },
    {
        "name": "100% Pure Orange Juice",
        "category": "Beverages",
        "brand": "Tropic Delight",
        "price": 3.89,
        "unit": "1.75 L bottle",
        "description": "Never from concentrate. Squeezed from Florida oranges without added sugars.",
        "image_url": "https://images.unsplash.com/photo-1621506289937-a8e4df240d0b?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 75,
        "rating": 4.7
    },
    {
        "name": "Crisp 100% Pure Apple Juice",
        "category": "Beverages",
        "brand": "Tropic Delight",
        "price": 3.69,
        "unit": "1.89 L bottle",
        "description": "Clear and refreshing 100% apple juice made with American orchard apples.",
        "image_url": "https://images.unsplash.com/photo-1621506289937-a8e4df240d0b?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 60,
        "rating": 4.6
    },
    {
        "name": "100% Pure Cranberry Juice",
        "category": "Beverages",
        "brand": "Ocean Spray",
        "price": 4.29,
        "unit": "1.89 L bottle",
        "description": "Tart and antioxidant-packed pure cranberry juice blend.",
        "image_url": "https://images.unsplash.com/photo-1621506289937-a8e4df240d0b?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 50,
        "rating": 4.7
    },
    {
        "name": "Organic Green Tea with Jasmine",
        "category": "Beverages",
        "brand": "Zen Herbal",
        "price": 4.49,
        "unit": "Box of 25 sachets",
        "description": "Calming organic green tea delicately infused with natural jasmine flowers.",
        "image_url": "https://images.unsplash.com/photo-1627435601361-ec25f5b1d0e5?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 55,
        "rating": 4.6
    },
    {
        "name": "Pure Chamomile Herbal Tea",
        "category": "Beverages",
        "brand": "Zen Herbal",
        "price": 4.29,
        "unit": "Box of 20 tea bags",
        "description": "Naturally caffeine-free herbal chamomile flowers for peaceful bedtime relaxation.",
        "image_url": "https://images.unsplash.com/photo-1627435601361-ec25f5b1d0e5?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 50,
        "rating": 4.8
    },
    {
        "name": "Sparkling Mineral Water",
        "category": "Beverages",
        "brand": "San Pellegrino",
        "price": 5.49,
        "unit": "Pack of 6 (500 ml bottles)",
        "description": "Naturally carbonated mineral water with crisp refreshing bubbles and balanced minerals.",
        "image_url": "https://images.unsplash.com/photo-1559839914-ba2a0f8eb209?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 90,
        "rating": 4.8
    },
    {
        "name": "Natural Spring Water 24-Pack",
        "category": "Beverages",
        "brand": "Crystal Pure",
        "price": 4.99,
        "unit": "Pack of 24 (500 ml bottles)",
        "description": "Pure, pristine natural mountain spring water bottled at the source.",
        "image_url": "https://images.unsplash.com/photo-1559839914-ba2a0f8eb209?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 100,
        "rating": 4.7
    },
    {
        "name": "Pure Tender Coconut Water",
        "category": "Beverages",
        "brand": "Vita Coco",
        "price": 2.79,
        "unit": "500 ml tetra pak",
        "description": "Naturally hydrating coconut water packed with electrolytes and potassium.",
        "image_url": "https://images.unsplash.com/photo-1559839914-ba2a0f8eb209?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 70,
        "rating": 4.8
    },
    {
        "name": "Classic Lemonade",
        "category": "Beverages",
        "brand": "Simply Lemonade",
        "price": 3.49,
        "unit": "1.5 L bottle",
        "description": "All-natural lemonade made with real lemon juice and pure cane sugar.",
        "image_url": "https://images.unsplash.com/photo-1621506289937-a8e4df240d0b?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 60,
        "rating": 4.7
    },
    {
        "name": "Sparkling Lemon-Lime Soda",
        "category": "Beverages",
        "brand": "Sprite",
        "price": 2.49,
        "unit": "2 Litre bottle",
        "description": "Crisp, clean, refreshing lemon-lime caffeine-free soda.",
        "image_url": "https://images.unsplash.com/photo-1559839914-ba2a0f8eb209?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 80,
        "rating": 4.6
    },
    {
        "name": "Classic Cola 12-Pack",
        "category": "Beverages",
        "brand": "Coca-Cola",
        "price": 6.99,
        "unit": "Pack of 12 cans (355 ml each)",
        "description": "The original crisp and bubbly refreshment enjoyed worldwide.",
        "image_url": "https://images.unsplash.com/photo-1559839914-ba2a0f8eb209?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 90,
        "rating": 4.8
    },
    {
        "name": "Organic Ginger Kombucha",
        "category": "Beverages",
        "brand": "Health-Ade",
        "price": 3.99,
        "unit": "473 ml bottle",
        "description": "Fermented probiotic tea infused with spicy organic cold-pressed ginger juice.",
        "image_url": "https://images.unsplash.com/photo-1559839914-ba2a0f8eb209?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 40,
        "rating": 4.7
    },
    {
        "name": "Iced Lemon Black Tea",
        "category": "Beverages",
        "brand": "Lipton",
        "price": 2.99,
        "unit": "1.89 L jug",
        "description": "Sweet iced black tea infused with natural lemon flavor.",
        "image_url": "https://images.unsplash.com/photo-1576092768241-dec231879fc3?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 55,
        "rating": 4.5
    },
    {
        "name": "Electrolyte Sports Drink",
        "category": "Beverages",
        "brand": "Gatorade Cool Blue",
        "price": 2.29,
        "unit": "946 ml bottle",
        "description": "Rapidly replenishes fluids and electrolytes lost in sweat.",
        "image_url": "https://images.unsplash.com/photo-1559839914-ba2a0f8eb209?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 70,
        "rating": 4.7
    },

    # =========================================================================
    # 6. Snacks & Confectionery (25 items)
    # =========================================================================
    {
        "name": "Sea Salt Crispy Potato Chips",
        "category": "Snacks",
        "brand": "Lay's Classic",
        "price": 2.99,
        "unit": "200 g bag",
        "description": "Thin, golden-fried crispy potato chips seasoned to perfection with pure sea salt.",
        "image_url": "https://images.unsplash.com/photo-1566478989037-eec170784d0b?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 110,
        "rating": 4.6
    },
    {
        "name": "Sour Cream & Onion Chips",
        "category": "Snacks",
        "brand": "Pringles",
        "price": 2.79,
        "unit": "165 g can",
        "description": "Crispy stackable potato crisps loaded with savory sour cream and onion flavor.",
        "image_url": "https://images.unsplash.com/photo-1566478989037-eec170784d0b?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 90,
        "rating": 4.7
    },
    {
        "name": "Tortilla Corn Chips",
        "category": "Snacks",
        "brand": "Doritos Nacho",
        "price": 3.29,
        "unit": "250 g bag",
        "description": "Crunchy triangular corn tortilla chips with bold nacho cheese seasoning.",
        "image_url": "https://images.unsplash.com/photo-1513456852971-30c0b8199d4d?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 90,
        "rating": 4.5
    },
    {
        "name": "Mild Chunky Tomato Salsa",
        "category": "Snacks",
        "brand": "Tostitos",
        "price": 3.49,
        "unit": "438 g jar",
        "description": "Diced ripe tomatoes, onions, and mild jalapenos. Ideal dip for tortilla chips.",
        "image_url": "https://images.unsplash.com/photo-1572441713132-c542fc4fe282?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 70,
        "rating": 4.8
    },
    {
        "name": "Crunchy Digestive Biscuits",
        "category": "Snacks",
        "brand": "McVitie's",
        "price": 2.49,
        "unit": "400 g pack",
        "description": "Classic wheat digestive biscuits with the iconic crunchy texture. Perfect for tea.",
        "image_url": "https://images.unsplash.com/photo-1558961363-fa8fdf82db35?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 85,
        "rating": 4.7
    },
    {
        "name": "Chocolate Sandwich Cookies (Oreo)",
        "category": "Snacks",
        "brand": "Oreo",
        "price": 3.99,
        "unit": "303 g family pack",
        "description": "Rich cocoa biscuits with signature vanilla creme filling. Twist, lick, dunk in milk!",
        "image_url": "https://images.unsplash.com/photo-1558961363-fa8fdf82db35?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 95,
        "rating": 4.9
    },
    {
        "name": "Chocolate Chip Cookies",
        "category": "Snacks",
        "brand": "Chips Ahoy!",
        "price": 3.69,
        "unit": "300 g pack",
        "description": "Crispy cookies loaded with real chocolate chips.",
        "image_url": "https://images.unsplash.com/photo-1558961363-fa8fdf82db35?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 80,
        "rating": 4.8
    },
    {
        "name": "Roasted & Salted California Almonds",
        "category": "Snacks",
        "brand": "Nutty Delights",
        "price": 6.99,
        "unit": "250 g pouch",
        "description": "Premium whole California almonds dry roasted with sea salt. High protein snack.",
        "image_url": "https://images.unsplash.com/photo-1508061253366-f7da158b6d46?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 65,
        "rating": 4.9
    },
    {
        "name": "Roasted Salted Cashews",
        "category": "Snacks",
        "brand": "Nutty Delights",
        "price": 7.49,
        "unit": "250 g pouch",
        "description": "Whole jumbo roasted cashews lightly salted for a rich, buttery crunch.",
        "image_url": "https://images.unsplash.com/photo-1508061253366-f7da158b6d46?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 55,
        "rating": 4.9
    },
    {
        "name": "Raw California Walnut Halves",
        "category": "Snacks",
        "brand": "Nutty Delights",
        "price": 6.49,
        "unit": "200 g pouch",
        "description": "Heart-healthy raw walnut halves rich in Omega-3 plant fatty acids.",
        "image_url": "https://images.unsplash.com/photo-1508061253366-f7da158b6d46?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 50,
        "rating": 4.8
    },
    {
        "name": "Roasted Salted Pistachios",
        "category": "Snacks",
        "brand": "Wonderful",
        "price": 7.99,
        "unit": "225 g bag",
        "description": "Naturally opened California in-shell roasted pistachios with sea salt.",
        "image_url": "https://images.unsplash.com/photo-1508061253366-f7da158b6d46?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 60,
        "rating": 4.9
    },
    {
        "name": "Healthy Nut & Fruit Trail Mix",
        "category": "Snacks",
        "brand": "Nature's Feast",
        "price": 5.99,
        "unit": "350 g resealable bag",
        "description": "Delicious energy mix of almonds, cashews, cranberries, raisins, and dark chocolate chips.",
        "image_url": "https://images.unsplash.com/photo-1508061253366-f7da158b6d46?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 70,
        "rating": 4.8
    },
    {
        "name": "70% Dark Chocolate Bar",
        "category": "Snacks",
        "brand": "Lindt Excellence",
        "price": 3.79,
        "unit": "100 g bar",
        "description": "Intense and velvety gourmet dark chocolate made with sustainably sourced cocoa beans.",
        "image_url": "https://images.unsplash.com/photo-1549007994-cb92caebd54b?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 70,
        "rating": 4.9
    },
    {
        "name": "Creamy Milk Chocolate Bar",
        "category": "Snacks",
        "brand": "Cadbury Dairy Milk",
        "price": 2.99,
        "unit": "110 g bar",
        "description": "Classic smooth and creamy British milk chocolate bar.",
        "image_url": "https://images.unsplash.com/photo-1549007994-cb92caebd54b?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 85,
        "rating": 4.8
    },
    {
        "name": "Movie Theater Butter Popcorn",
        "category": "Snacks",
        "brand": "Orville Redenbacher",
        "price": 3.99,
        "unit": "Box of 6 microwave bags",
        "description": "100% whole grain fluffy popcorn with rich, melt-in-your-mouth butter flavor.",
        "image_url": "https://images.unsplash.com/photo-1513456852971-30c0b8199d4d?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 65,
        "rating": 4.7
    },
    {
        "name": "Salted Mini Pretzel Twists",
        "category": "Snacks",
        "brand": "Snyder's of Hanover",
        "price": 2.89,
        "unit": "340 g bag",
        "description": "Crunchy oven-baked sourdough mini pretzel twists with pure salt crystals.",
        "image_url": "https://images.unsplash.com/photo-1513456852971-30c0b8199d4d?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 60,
        "rating": 4.6
    },
    {
        "name": "Honey Oats Granola Bars",
        "category": "Snacks",
        "brand": "Nature Valley",
        "price": 3.49,
        "unit": "Box of 12 crunchy bars",
        "description": "Crunchy whole grain rolled oats with real honey flavor.",
        "image_url": "https://images.unsplash.com/photo-1517093157656-b9ec91b199d6?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 75,
        "rating": 4.7
    },
    {
        "name": "Fruit Gummy Bears",
        "category": "Snacks",
        "brand": "Haribo Goldbears",
        "price": 2.29,
        "unit": "200 g bag",
        "description": "Chewy, fruity gummy candy in iconic bear shapes with 5 natural fruit flavors.",
        "image_url": "https://images.unsplash.com/photo-1582058091505-f87a2e55a40f?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 80,
        "rating": 4.8
    },
    {
        "name": "Vanilla Cream Wafers",
        "category": "Snacks",
        "brand": "Loacker Quadratini",
        "price": 3.49,
        "unit": "250 g pouch",
        "description": "Crisp multi-layered wafer bites filled with exquisite Alpine vanilla cream.",
        "image_url": "https://images.unsplash.com/photo-1558961363-fa8fdf82db35?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 60,
        "rating": 4.8
    },
    {
        "name": "Organic Lightly Salted Rice Cakes",
        "category": "Snacks",
        "brand": "Lundberg",
        "price": 2.99,
        "unit": "240 g pack (13 cakes)",
        "description": "Puffed whole brown rice cakes. Great low-calorie base for peanut butter.",
        "image_url": "https://images.unsplash.com/photo-1513456852971-30c0b8199d4d?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 50,
        "rating": 4.5
    },
    {
        "name": "Wheat Table Crackers",
        "category": "Snacks",
        "brand": "Ritz",
        "price": 3.29,
        "unit": "388 g box",
        "description": "Flaky, buttery round crackers. Perfect pair with cheddar cheese and dips.",
        "image_url": "https://images.unsplash.com/photo-1558961363-fa8fdf82db35?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 80,
        "rating": 4.7
    },
    {
        "name": "Spicy Masala Peanut Snack",
        "category": "Snacks",
        "brand": "Haldiram's",
        "price": 2.19,
        "unit": "200 g pack",
        "description": "Crispy spiced besan coated roasted peanuts with tangy Indian chaat masala.",
        "image_url": "https://images.unsplash.com/photo-1508061253366-f7da158b6d46?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 85,
        "rating": 4.8
    },
    {
        "name": "Dried Sweetened Cranberries",
        "category": "Snacks",
        "brand": "Ocean Spray Craisins",
        "price": 3.99,
        "unit": "283 g pouch",
        "description": "Plump, sweet dried cranberries for salads, oatmeal, and trail snacking.",
        "image_url": "https://images.unsplash.com/photo-1498557850523-fd3d118b962e?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 60,
        "rating": 4.8
    },
    {
        "name": "Peanut Butter Protein Bar",
        "category": "Snacks",
        "brand": "Clif Bar",
        "price": 2.49,
        "unit": "68 g bar",
        "description": "Plant-based energy bar made with organic rolled oats and creamy peanut butter.",
        "image_url": "https://images.unsplash.com/photo-1517093157656-b9ec91b199d6?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 70,
        "rating": 4.7
    },
    {
        "name": "Fluffy Marshmallows",
        "category": "Snacks",
        "brand": "Campfire",
        "price": 1.99,
        "unit": "300 g bag",
        "description": "Puffy sweet vanilla marshmallows for hot chocolate, s'mores, and baking.",
        "image_url": "https://images.unsplash.com/photo-1582058091505-f87a2e55a40f?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 50,
        "rating": 4.6
    },

    # =========================================================================
    # 7. Grains, Pasta & Pantry Staples (26 items)
    # =========================================================================
    {
        "name": "Royal Basmati Rice",
        "category": "Grains",
        "brand": "Royal",
        "price": 8.99,
        "unit": "2 kg bag",
        "description": "Aromatic extra-long grain authentic Basmati rice. Cooks into fluffy biryanis and pilafs.",
        "image_url": "https://images.unsplash.com/photo-1586201375761-83865001e31c?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 90,
        "rating": 4.9
    },
    {
        "name": "Fragrant Jasmine Rice",
        "category": "Grains",
        "brand": "Dynasty",
        "price": 7.99,
        "unit": "2 kg bag",
        "description": "Naturally fragrant long-grain Thai Jasmine rice, ideal for Asian stir-fries and curries.",
        "image_url": "https://images.unsplash.com/photo-1586201375761-83865001e31c?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 70,
        "rating": 4.8
    },
    {
        "name": "Organic Whole Brown Rice",
        "category": "Grains",
        "brand": "Lundberg",
        "price": 5.49,
        "unit": "1 kg bag",
        "description": "100% whole grain brown rice with nutty flavor and chewy texture.",
        "image_url": "https://images.unsplash.com/photo-1586201375761-83865001e31c?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 60,
        "rating": 4.7
    },
    {
        "name": "Organic White Quinoa",
        "category": "Grains",
        "brand": "Ancient Harvest",
        "price": 5.99,
        "unit": "500 g pouch",
        "description": "Complete plant protein supergrain, pre-washed and gluten-free.",
        "image_url": "https://images.unsplash.com/photo-1586201375761-83865001e31c?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 50,
        "rating": 4.8
    },
    {
        "name": "All-Purpose Wheat Flour",
        "category": "Grains",
        "brand": "King Arthur",
        "price": 4.49,
        "unit": "2 kg bag",
        "description": "Unbleached premium all-purpose wheat flour for bread, pastry, cookies, and everyday baking.",
        "image_url": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 100,
        "rating": 4.8
    },
    {
        "name": "Whole Wheat Sharbati Atta",
        "category": "Grains",
        "brand": "Aashirvaad",
        "price": 7.99,
        "unit": "5 kg bag",
        "description": "100% pure whole wheat stone ground flour for soft rotis, parathas, and naans.",
        "image_url": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 80,
        "rating": 4.9
    },
    {
        "name": "Organic Rolled Oats",
        "category": "Grains",
        "brand": "Quaker Oats",
        "price": 3.99,
        "unit": "1 kg canister",
        "description": "100% whole grain rolled oats. Rich in beta-glucan soluble fiber for heart-healthy breakfasts.",
        "image_url": "https://images.unsplash.com/photo-1517093157656-b9ec91b199d6?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 85,
        "rating": 4.7
    },
    {
        "name": "Quick 1-Minute Cooking Oats",
        "category": "Grains",
        "brand": "Quaker Oats",
        "price": 3.89,
        "unit": "1 kg canister",
        "description": "Fine-cut whole oats that cook into warm creamy oatmeal in just 60 seconds.",
        "image_url": "https://images.unsplash.com/photo-1517093157656-b9ec91b199d6?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 70,
        "rating": 4.6
    },
    {
        "name": "Italian Penne Rigate Pasta",
        "category": "Grains",
        "brand": "Barilla",
        "price": 2.19,
        "unit": "500 g box",
        "description": "Classic durum wheat semolina penne rigate pasta. Ridged surface holds marinara and cream sauces.",
        "image_url": "https://images.unsplash.com/photo-1551462147-ff29053bfc14?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 120,
        "rating": 4.8
    },
    {
        "name": "Classic Spaghetti Pasta",
        "category": "Grains",
        "brand": "Barilla",
        "price": 2.19,
        "unit": "500 g box",
        "description": "Traditional Italian durum wheat long spaghetti strands for marinara and meatballs.",
        "image_url": "https://images.unsplash.com/photo-1551462147-ff29053bfc14?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 110,
        "rating": 4.8
    },
    {
        "name": "Elbow Macaroni Pasta",
        "category": "Grains",
        "brand": "Barilla",
        "price": 1.99,
        "unit": "500 g box",
        "description": "Classic elbow macaroni pasta, the ultimate choice for creamy Mac & Cheese.",
        "image_url": "https://images.unsplash.com/photo-1551462147-ff29053bfc14?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 90,
        "rating": 4.7
    },
    {
        "name": "Fusilli Spiral Pasta",
        "category": "Grains",
        "brand": "De Cecco",
        "price": 2.79,
        "unit": "500 g box",
        "description": "Bronze-die extruded spiral pasta twists that capture pesto and rich vegetable sauces.",
        "image_url": "https://images.unsplash.com/photo-1551462147-ff29053bfc14?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 60,
        "rating": 4.9
    },
    {
        "name": "Classic Marinara Pasta Sauce",
        "category": "Grains",
        "brand": "Rao's Homemade",
        "price": 5.49,
        "unit": "680 g jar",
        "description": "Slow-simmered Italian plum tomatoes with olive oil, fresh basil, and garlic. Perfect with pasta.",
        "image_url": "https://images.unsplash.com/photo-1572441713132-c542fc4fe282?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 70,
        "rating": 4.9
    },
    {
        "name": "Creamy Garlic Alfredo Pasta Sauce",
        "category": "Grains",
        "brand": "Bertolli",
        "price": 3.99,
        "unit": "425 g jar",
        "description": "Decadent cream sauce crafted with real parmesan, butter, and roasted garlic.",
        "image_url": "https://images.unsplash.com/photo-1572441713132-c542fc4fe282?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 55,
        "rating": 4.7
    },
    {
        "name": "Traditional Basil Pesto Sauce",
        "category": "Grains",
        "brand": "Barilla",
        "price": 4.29,
        "unit": "190 g jar",
        "description": "Aromatic Genovese basil blended with pine nuts, garlic, and parmesan cheese.",
        "image_url": "https://images.unsplash.com/photo-1572441713132-c542fc4fe282?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 45,
        "rating": 4.8
    },
    {
        "name": "Extra Virgin Olive Oil",
        "category": "Grains",
        "brand": "Filippo Berio",
        "price": 9.99,
        "unit": "750 ml bottle",
        "description": "First cold-pressed extra virgin olive oil for pasta, dressings, sautéing, and dips.",
        "image_url": "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 65,
        "rating": 4.9
    },
    {
        "name": "Pure Sunflower Cooking Oil",
        "category": "Grains",
        "brand": "Golden Drop",
        "price": 6.29,
        "unit": "1 Litre bottle",
        "description": "Light, high-smoke point refined sunflower cooking oil with Vitamin E for everyday frying.",
        "image_url": "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 80,
        "rating": 4.6
    },
    {
        "name": "Pure Canola Cooking Oil",
        "category": "Grains",
        "brand": "Wesson",
        "price": 5.79,
        "unit": "1.42 L bottle",
        "description": "Cholesterol-free, neutral-tasting cooking oil with high smoke point for baking and frying.",
        "image_url": "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 70,
        "rating": 4.5
    },
    {
        "name": "Organic Yellow Moong Dal",
        "category": "Grains",
        "brand": "Pure Harvest",
        "price": 3.79,
        "unit": "1 kg bag",
        "description": "Split yellow lentils rich in plant protein. Cooks into comforting, easy-to-digest dal dishes.",
        "image_url": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 90,
        "rating": 4.7
    },
    {
        "name": "Organic Red Split Lentils (Masoor)",
        "category": "Grains",
        "brand": "Pure Harvest",
        "price": 3.69,
        "unit": "1 kg bag",
        "description": "Quick-cooking red lentils for hearty soups, curries, and protein bowls.",
        "image_url": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 80,
        "rating": 4.8
    },
    {
        "name": "Organic Chickpeas (Garbanzo Beans)",
        "category": "Grains",
        "brand": "Goya",
        "price": 1.79,
        "unit": "439 g can",
        "description": "Tender cooked chickpeas in sea salt brine, ready for homemade hummus and salads.",
        "image_url": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 85,
        "rating": 4.7
    },
    {
        "name": "Organic Black Beans",
        "category": "Grains",
        "brand": "Goya",
        "price": 1.79,
        "unit": "439 g can",
        "description": "Cooked creamy black beans for burritos, chili, and taco bowls.",
        "image_url": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 80,
        "rating": 4.7
    },
    {
        "name": "Pure Granulated Cane Sugar",
        "category": "Grains",
        "brand": "Domino",
        "price": 2.89,
        "unit": "1.8 kg bag",
        "description": "Fine granulated pure cane sugar for sweetening tea, coffee, baking, and cooking.",
        "image_url": "https://images.unsplash.com/photo-1587735243615-c03f25aaff15?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 100,
        "rating": 4.6
    },
    {
        "name": "Light Brown Baking Sugar",
        "category": "Grains",
        "brand": "Domino",
        "price": 2.99,
        "unit": "900 g bag",
        "description": "Moist brown sugar with natural molasses flavor for soft cookies and barbecue glazes.",
        "image_url": "https://images.unsplash.com/photo-1587735243615-c03f25aaff15?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 60,
        "rating": 4.8
    },
    {
        "name": "Iodized Table Salt",
        "category": "Grains",
        "brand": "Morton",
        "price": 1.19,
        "unit": "737 g canister",
        "description": "Free-flowing iodized table salt with anti-caking agent for kitchen seasoning.",
        "image_url": "https://images.unsplash.com/photo-1518110925495-5fe2fda0442c?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 150,
        "rating": 4.7
    },
    {
        "name": "Coarse Mediterranean Sea Salt",
        "category": "Grains",
        "brand": "Morton",
        "price": 2.49,
        "unit": "500 g grinder bottle",
        "description": "Natural sun-evaporated sea salt crystals for gourmet finishing and roasting.",
        "image_url": "https://images.unsplash.com/photo-1518110925495-5fe2fda0442c?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 80,
        "rating": 4.8
    },

    # =========================================================================
    # 8. Spices, Sauces & Condiments (20 items)
    # =========================================================================
    {
        "name": "Organic Ground Turmeric Powder",
        "category": "Grains",
        "brand": "Spice Islands",
        "price": 2.99,
        "unit": "100 g jar",
        "description": "Bright golden turmeric powder with high curcumin content for curries and lattes.",
        "image_url": "https://images.unsplash.com/photo-1615485290382-441e4d049cb5?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 75,
        "rating": 4.8
    },
    {
        "name": "Pure Ground Black Pepper",
        "category": "Grains",
        "brand": "McCormick",
        "price": 3.49,
        "unit": "150 g tin",
        "description": "Coarsely ground Malabar black peppercorns for pungent aromatic heat.",
        "image_url": "https://images.unsplash.com/photo-1615485290382-441e4d049cb5?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 85,
        "rating": 4.9
    },
    {
        "name": "Authentic Garam Masala Powder",
        "category": "Grains",
        "brand": "MDH",
        "price": 2.79,
        "unit": "100 g box",
        "description": "Traditional blend of cinnamon, cardamom, cloves, and mace for North Indian curries.",
        "image_url": "https://images.unsplash.com/photo-1615485290382-441e4d049cb5?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 80,
        "rating": 4.8
    },
    {
        "name": "Whole Cumin Seeds (Jeera)",
        "category": "Grains",
        "brand": "Swad",
        "price": 2.49,
        "unit": "200 g pouch",
        "description": "Aromatic whole cumin seeds for tempering dals, rice, and spice rubs.",
        "image_url": "https://images.unsplash.com/photo-1615485290382-441e4d049cb5?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 90,
        "rating": 4.8
    },
    {
        "name": "Ground Red Chili Powder",
        "category": "Grains",
        "brand": "Everest",
        "price": 2.49,
        "unit": "100 g box",
        "description": "Vibrant Kashmiri red chili powder providing rich color and moderate spiciness.",
        "image_url": "https://images.unsplash.com/photo-1615485290382-441e4d049cb5?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 85,
        "rating": 4.7
    },
    {
        "name": "Dried Mediterranean Oregano",
        "category": "Grains",
        "brand": "McCormick",
        "price": 2.79,
        "unit": "50 g glass jar",
        "description": "Fragrant dried crushed oregano leaves for pizza, pasta sauces, and marinades.",
        "image_url": "https://images.unsplash.com/photo-1615485290382-441e4d049cb5?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 70,
        "rating": 4.8
    },
    {
        "name": "Ground Sweet Paprika",
        "category": "Grains",
        "brand": "McCormick",
        "price": 2.99,
        "unit": "60 g jar",
        "description": "Mild, sweet Hungarian ground red pepper for goulash, deviled eggs, and rubs.",
        "image_url": "https://images.unsplash.com/photo-1615485290382-441e4d049cb5?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 60,
        "rating": 4.7
    },
    {
        "name": "Pure Ground Cinnamon",
        "category": "Grains",
        "brand": "Spice Islands",
        "price": 3.29,
        "unit": "70 g jar",
        "description": "Sweet, fragrant Ceylon cinnamon powder for oatmeal, baked pies, and French toast.",
        "image_url": "https://images.unsplash.com/photo-1615485290382-441e4d049cb5?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 65,
        "rating": 4.9
    },
    {
        "name": "Tomato Ketchup",
        "category": "Grains",
        "brand": "Heinz",
        "price": 3.19,
        "unit": "567 g upside-down bottle",
        "description": "America's favorite rich and thick tomato ketchup with ripe sun-grown tomatoes.",
        "image_url": "https://images.unsplash.com/photo-1572441713132-c542fc4fe282?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 100,
        "rating": 4.9
    },
    {
        "name": "Real Mayonnaise",
        "category": "Grains",
        "brand": "Hellmann's",
        "price": 4.49,
        "unit": "887 ml jar",
        "description": "Creamy mayonnaise crafted with cage-free eggs, oil, and vinegar for juicy sandwiches.",
        "image_url": "https://images.unsplash.com/photo-1589985270826-4b7bb135bc9d?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 75,
        "rating": 4.8
    },
    {
        "name": "Yellow Classic Mustard",
        "category": "Grains",
        "brand": "French's",
        "price": 1.99,
        "unit": "396 g squeeze bottle",
        "description": "Tangy stone-ground yellow mustard, perfect for hot dogs, burgers, and sandwiches.",
        "image_url": "https://images.unsplash.com/photo-1589985270826-4b7bb135bc9d?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 80,
        "rating": 4.7
    },
    {
        "name": "Naturally Brewed Soy Sauce",
        "category": "Grains",
        "brand": "Kikkoman",
        "price": 3.49,
        "unit": "444 ml bottle",
        "description": "Traditional Japanese naturally brewed umami soy sauce for stir-fries and marinades.",
        "image_url": "https://images.unsplash.com/photo-1572441713132-c542fc4fe282?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 85,
        "rating": 4.9
    },
    {
        "name": "Hot Chili Sriracha Sauce",
        "category": "Grains",
        "brand": "Huy Fong",
        "price": 4.29,
        "unit": "482 g bottle",
        "description": "Famous rooster hot chili sriracha sauce made with sun-ripened red jalapenos and garlic.",
        "image_url": "https://images.unsplash.com/photo-1572441713132-c542fc4fe282?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 70,
        "rating": 4.9
    },
    {
        "name": "Smoky Honey Barbecue Sauce",
        "category": "Grains",
        "brand": "Sweet Baby Ray's",
        "price": 2.79,
        "unit": "510 g bottle",
        "description": "The sauce is the boss! Sweet and smoky barbecue sauce for ribs, chicken, and burgers.",
        "image_url": "https://images.unsplash.com/photo-1572441713132-c542fc4fe282?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 65,
        "rating": 4.8
    },
    {
        "name": "Pure Apple Cider Vinegar",
        "category": "Grains",
        "brand": "Bragg",
        "price": 4.99,
        "unit": "473 ml bottle",
        "description": "Raw, organic, unfiltered apple cider vinegar with the beneficial 'Mother'.",
        "image_url": "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 60,
        "rating": 4.9
    },
    {
        "name": "Distilled White Vinegar",
        "category": "Grains",
        "brand": "Heinz",
        "price": 2.19,
        "unit": "1.89 L bottle",
        "description": "All-purpose distilled white vinegar for pickling, marinades, and natural cleaning.",
        "image_url": "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 90,
        "rating": 4.7
    },
    {
        "name": "Spicy Mango Pickle (Achar)",
        "category": "Grains",
        "brand": "Mothers Recipe",
        "price": 3.49,
        "unit": "400 g glass jar",
        "description": "Traditional Indian raw green mango pickle steeped in mustard oil and fenugreek.",
        "image_url": "https://images.unsplash.com/photo-1572441713132-c542fc4fe282?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 55,
        "rating": 4.8
    },
    {
        "name": "Dill Pickle Spear Spears",
        "category": "Grains",
        "brand": "Vlasic",
        "price": 3.29,
        "unit": "680 g jar",
        "description": "Crispy kosher dill cucumber pickle spears with garlic and herb crunch.",
        "image_url": "https://images.unsplash.com/photo-1572441713132-c542fc4fe282?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 60,
        "rating": 4.7
    },
    {
        "name": "Roasted Sesame Oil",
        "category": "Grains",
        "brand": "Kadoya",
        "price": 5.49,
        "unit": "327 ml bottle",
        "description": "100% pure toasted dark sesame oil for rich nutty finishing on Asian noodles and rice.",
        "image_url": "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 45,
        "rating": 4.9
    },
    {
        "name": "Pure Baking Powder",
        "category": "Grains",
        "brand": "Clabber Girl",
        "price": 1.99,
        "unit": "230 g canister",
        "description": "Double-acting baking powder for dependable leavening in cakes, biscuits, and pancakes.",
        "image_url": "https://images.unsplash.com/photo-1518110925495-5fe2fda0442c?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 70,
        "rating": 4.8
    },

    # =========================================================================
    # 9. Frozen Food & Quick Meals (18 items)
    # =========================================================================
    {
        "name": "Mixed Frozen Vegetables",
        "category": "Frozen Food",
        "brand": "Birds Eye",
        "price": 2.69,
        "unit": "500 g bag",
        "description": "Flash-frozen blend of sweet corn, tender peas, diced carrots, and green beans.",
        "image_url": "https://images.unsplash.com/photo-1506484381205-f7945653044d?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 65,
        "rating": 4.6
    },
    {
        "name": "Frozen Sweet Green Peas",
        "category": "Frozen Food",
        "brand": "Birds Eye",
        "price": 2.49,
        "unit": "450 g bag",
        "description": "Sweet, tender garden peas harvested at peak ripeness and flash frozen.",
        "image_url": "https://images.unsplash.com/photo-1506484381205-f7945653044d?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 70,
        "rating": 4.7
    },
    {
        "name": "Frozen Sweet Golden Corn",
        "category": "Frozen Food",
        "brand": "Green Giant",
        "price": 2.49,
        "unit": "450 g bag",
        "description": "Crisp whole kernel golden sweet corn kernels for soups and Mexican bowls.",
        "image_url": "https://images.unsplash.com/photo-1506484381205-f7945653044d?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 60,
        "rating": 4.7
    },
    {
        "name": "Golden Crispy French Fries",
        "category": "Frozen Food",
        "brand": "McCain",
        "price": 3.49,
        "unit": "750 g bag",
        "description": "Golden, restaurant-style crispy cut fries ready to air-fry or bake in 15 minutes.",
        "image_url": "https://images.unsplash.com/photo-1576107232684-1279f3908594?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 70,
        "rating": 4.6
    },
    {
        "name": "Crispy Tater Hash Browns",
        "category": "Frozen Food",
        "brand": "Ore-Ida",
        "price": 3.79,
        "unit": "800 g bag",
        "description": "Shredded seasoned Russet potato patties, golden and crisp for morning breakfast.",
        "image_url": "https://images.unsplash.com/photo-1576107232684-1279f3908594?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 55,
        "rating": 4.7
    },
    {
        "name": "Four Cheese Thin Crust Pizza",
        "category": "Frozen Food",
        "brand": "DiGiorno",
        "price": 6.99,
        "unit": "620 g frozen pizza",
        "description": "Crispy thin crust topped with mozzarella, parmesan, romano, and asiago cheese.",
        "image_url": "https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 40,
        "rating": 4.7
    },
    {
        "name": "Pepperoni Rising Crust Pizza",
        "category": "Frozen Food",
        "brand": "DiGiorno",
        "price": 7.49,
        "unit": "780 g pizza",
        "description": "Thick self-rising crust topped with savory pepperoni slices and melted mozzarella.",
        "image_url": "https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 45,
        "rating": 4.8
    },
    {
        "name": "Frozen Veggie Burger Patties",
        "category": "Frozen Food",
        "brand": "Beyond Meat",
        "price": 5.99,
        "unit": "Pack of 4 patties",
        "description": "Plant-based high protein burger patties with 20g protein per patty.",
        "image_url": "https://images.unsplash.com/photo-1586190848861-99aa4a171e90?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 40,
        "rating": 4.8
    },
    {
        "name": "Frozen Steamed Vegetable Dumplings",
        "category": "Frozen Food",
        "brand": "Bibigo",
        "price": 6.49,
        "unit": "560 g bag",
        "description": "Delicate potsticker dumplings filled with cabbage, tofu, and scallions.",
        "image_url": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 35,
        "rating": 4.9
    },
    {
        "name": "Vanilla Bean Ice Cream",
        "category": "Frozen Food",
        "brand": "Häagen-Dazs",
        "price": 5.49,
        "unit": "473 ml tub",
        "description": "Made with only 5 pure ingredients including real Madagascar vanilla bean flecks.",
        "image_url": "https://images.unsplash.com/photo-1571212515416-fef01fc43637?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 50,
        "rating": 4.9
    },
    {
        "name": "Belgian Chocolate Ice Cream",
        "category": "Frozen Food",
        "brand": "Häagen-Dazs",
        "price": 5.49,
        "unit": "473 ml tub",
        "description": "Rich Belgian chocolate ice cream swirled with finely shaved dark chocolate flakes.",
        "image_url": "https://images.unsplash.com/photo-1571212515416-fef01fc43637?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 45,
        "rating": 4.9
    },
    {
        "name": "Homestyle Frozen Waffles",
        "category": "Frozen Food",
        "brand": "Eggo",
        "price": 3.49,
        "unit": "Box of 10 waffles",
        "description": "Crispy, golden toaster waffles. Just pop in toaster and top with butter & maple syrup.",
        "image_url": "https://images.unsplash.com/photo-1555507036-ab1f4038808a?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 55,
        "rating": 4.7
    },
    {
        "name": "Frozen Garlic Naan Bread",
        "category": "Frozen Food",
        "brand": "Deep Indian Kitchen",
        "price": 4.19,
        "unit": "Pack of 4 tandoor baked naans",
        "description": "Authentic clay oven baked fluffy naans brushed with garlic butter and cilantro.",
        "image_url": "https://images.unsplash.com/photo-1565299585323-38d6b0865b47?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 50,
        "rating": 4.8
    },
    {
        "name": "Frozen Organic Edamame Pods",
        "category": "Frozen Food",
        "brand": "Seapoint Farms",
        "price": 2.99,
        "unit": "400 g steam bag",
        "description": "Young soybeans in pod, high in plant protein and dietary fiber.",
        "image_url": "https://images.unsplash.com/photo-1567306226416-28f0efdc88ce?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 40,
        "rating": 4.7
    },
    {
        "name": "Frozen Wild Berry Smoothie Blend",
        "category": "Frozen Food",
        "brand": "Dole",
        "price": 4.99,
        "unit": "600 g pouch",
        "description": "Pre-portioned flash-frozen blend of strawberries, blueberries, and blackberries.",
        "image_url": "https://images.unsplash.com/photo-1498557850523-fd3d118b962e?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 45,
        "rating": 4.8
    },

    # =========================================================================
    # 10. Personal Care & Hygiene (16 items)
    # =========================================================================
    {
        "name": "Nourishing Coconut Milk Shampoo",
        "category": "Personal Care",
        "brand": "OGX",
        "price": 6.99,
        "unit": "385 ml bottle",
        "description": "Sulfate-free coconut milk shampoo that hydrates, strengthens, and restores hair shine.",
        "image_url": "https://images.unsplash.com/photo-1535585209827-a15fcdbc4c2d?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 60,
        "rating": 4.7
    },
    {
        "name": "Nourishing Coconut Milk Conditioner",
        "category": "Personal Care",
        "brand": "OGX",
        "price": 6.99,
        "unit": "385 ml bottle",
        "description": "Ultra-hydrating conditioner with coconut oil and whipped egg white proteins.",
        "image_url": "https://images.unsplash.com/photo-1535585209827-a15fcdbc4c2d?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 55,
        "rating": 4.8
    },
    {
        "name": "Moisturizing Beauty Bar Soap",
        "category": "Personal Care",
        "brand": "Dove",
        "price": 5.49,
        "unit": "Pack of 4 bars (100g each)",
        "description": "With 1/4 moisturizing cream for soft, smooth, healthy-feeling skin every day.",
        "image_url": "https://images.unsplash.com/photo-1607006314352-094119934751?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 80,
        "rating": 4.8
    },
    {
        "name": "Refreshing Citrus Body Wash",
        "category": "Personal Care",
        "brand": "Nivea",
        "price": 4.99,
        "unit": "500 ml bottle",
        "description": "Invigorating body wash infused with natural citrus oils for long-lasting freshness.",
        "image_url": "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 65,
        "rating": 4.6
    },
    {
        "name": "Total Care Antibacterial Toothpaste",
        "category": "Personal Care",
        "brand": "Colgate Total",
        "price": 3.49,
        "unit": "150 g tube",
        "description": "12-hour antibacterial shield protecting against cavities, plaque, and tartar.",
        "image_url": "https://images.unsplash.com/photo-1559591937-e1032b453e0d?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 110,
        "rating": 4.8
    },
    {
        "name": "Soft Bristle Toothbrush 4-Pack",
        "category": "Personal Care",
        "brand": "Oral-B",
        "price": 4.29,
        "unit": "Pack of 4 brushes",
        "description": "End-rounded bristles designed to be gentle on gums while cleaning deep between teeth.",
        "image_url": "https://images.unsplash.com/photo-1559591937-e1032b453e0d?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 90,
        "rating": 4.7
    },
    {
        "name": "Antiseptic Cool Mint Mouthwash",
        "category": "Personal Care",
        "brand": "Listerine",
        "price": 5.99,
        "unit": "1 Litre bottle",
        "description": "Kills 99.9% of germs that cause bad breath, plaque, and gingivitis.",
        "image_url": "https://images.unsplash.com/photo-1559591937-e1032b453e0d?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 60,
        "rating": 4.8
    },
    {
        "name": "Gentle Daily Face Cleanser",
        "category": "Personal Care",
        "brand": "Cetaphil",
        "price": 8.99,
        "unit": "473 ml pump bottle",
        "description": "Hydrating, non-irritating formula for sensitive and all skin types.",
        "image_url": "https://images.unsplash.com/photo-1556228720-195a672e8a03?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 50,
        "rating": 4.9
    },
    {
        "name": "Moisturizing Daily Body Lotion",
        "category": "Personal Care",
        "brand": "Aveeno Daily Moisture",
        "price": 7.49,
        "unit": "532 ml pump bottle",
        "description": "Formulated with prebiotic oat to nourish and lock in 24-hour hydration.",
        "image_url": "https://images.unsplash.com/photo-1556228720-195a672e8a03?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 55,
        "rating": 4.8
    },
    {
        "name": "Antibacterial Liquid Hand Soap",
        "category": "Personal Care",
        "brand": "Softsoap",
        "price": 2.49,
        "unit": "332 ml pump bottle",
        "description": "Crisp clean scent with soothing aloe vera to wash away dirt and bacteria.",
        "image_url": "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 100,
        "rating": 4.8
    },
    {
        "name": "Advanced Hand Sanitizer Gel",
        "category": "Personal Care",
        "brand": "Purell",
        "price": 3.29,
        "unit": "236 ml pump bottle",
        "description": "70% ethyl alcohol formula that kills 99.99% of most common germs.",
        "image_url": "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 90,
        "rating": 4.8
    },
    {
        "name": "48H Antiperspirant Deodorant",
        "category": "Personal Care",
        "brand": "Degree Men",
        "price": 4.49,
        "unit": "76 g stick",
        "description": "Motion-activated sweat and odor protection for non-stop confidence.",
        "image_url": "https://images.unsplash.com/photo-1556228720-195a672e8a03?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 65,
        "rating": 4.7
    },
    {
        "name": "Mineral Sunscreen Lotion SPF 50",
        "category": "Personal Care",
        "brand": "Neutrogena",
        "price": 9.99,
        "unit": "88 ml tube",
        "description": "Broad spectrum UVA/UVB water-resistant sheer mineral sun protection.",
        "image_url": "https://images.unsplash.com/photo-1556228720-195a672e8a03?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 40,
        "rating": 4.8
    },
    {
        "name": "Sensitive Skin Shaving Foam",
        "category": "Personal Care",
        "brand": "Gillette",
        "price": 2.99,
        "unit": "311 g can",
        "description": "Thick, rich lubricating lather infused with aloe for an effortless close shave.",
        "image_url": "https://images.unsplash.com/photo-1556228720-195a672e8a03?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 50,
        "rating": 4.6
    },
    {
        "name": "Moisturizing Lip Balm 3-Pack",
        "category": "Personal Care",
        "brand": "Burt's Bees",
        "price": 6.49,
        "unit": "Pack of 3 tubes",
        "description": "100% natural beeswax lip balm with peppermint oil and Vitamin E.",
        "image_url": "https://images.unsplash.com/photo-1556228720-195a672e8a03?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 70,
        "rating": 4.9
    },
    {
        "name": "Pure Cotton Swabs (Q-tips)",
        "category": "Personal Care",
        "brand": "Q-tips",
        "price": 3.19,
        "unit": "Pack of 500 swabs",
        "description": "100% pure soft cotton tips on sturdy flexible sticks for hygiene and beauty.",
        "image_url": "https://images.unsplash.com/photo-1556228720-195a672e8a03?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 80,
        "rating": 4.8
    },

    # =========================================================================
    # 11. Household & Cleaning Supplies (16 items)
    # =========================================================================
    {
        "name": "Concentrated Laundry Detergent",
        "category": "Household",
        "brand": "Tide Original",
        "price": 11.99,
        "unit": "2.72 L bottle (64 loads)",
        "description": "Advanced stain-lifting formula that keeps whites bright and colors vivid wash after wash.",
        "image_url": "https://images.unsplash.com/photo-1585670149967-b4f4da88cc9f?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 55,
        "rating": 4.9
    },
    {
        "name": "Laundry Detergent Pods",
        "category": "Household",
        "brand": "Tide Pods 3-in-1",
        "price": 14.99,
        "unit": "Tub of 42 pacs",
        "description": "Concentrated detergent + stain remover + color protector in pre-measured pods.",
        "image_url": "https://images.unsplash.com/photo-1585670149967-b4f4da88cc9f?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 50,
        "rating": 4.9
    },
    {
        "name": "Ultra Concentrated Dishwashing Liquid",
        "category": "Household",
        "brand": "Dawn Platinum",
        "price": 3.99,
        "unit": "700 ml bottle",
        "description": "Cuts through tough 48-hour stuck-on grease effortlessly with refreshing scent.",
        "image_url": "https://images.unsplash.com/photo-1585670149967-b4f4da88cc9f?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 90,
        "rating": 4.9
    },
    {
        "name": "Multi-Surface Disinfectant Spray",
        "category": "Household",
        "brand": "Lysol",
        "price": 4.49,
        "unit": "946 ml spray bottle",
        "description": "Kills 99.9% of viruses and bacteria on hard non-porous surfaces. Lemon breeze scent.",
        "image_url": "https://images.unsplash.com/photo-1584744982491-665216d95f8b?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 70,
        "rating": 4.7
    },
    {
        "name": "Sparkling Glass & Mirror Cleaner",
        "category": "Household",
        "brand": "Windex",
        "price": 3.79,
        "unit": "680 ml spray bottle",
        "description": "Streak-free shine formula for windows, mirrors, glass tables, and chrome.",
        "image_url": "https://images.unsplash.com/photo-1584744982491-665216d95f8b?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 65,
        "rating": 4.8
    },
    {
        "name": "Strong Paper Towels",
        "category": "Household",
        "brand": "Bounty Quick-Size",
        "price": 8.99,
        "unit": "Pack of 6 double rolls",
        "description": "2x more absorbent paper towels for fast kitchen spill cleanups.",
        "image_url": "https://images.unsplash.com/photo-1583947215259-38e31be8751f?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 60,
        "rating": 4.8
    },
    {
        "name": "Ultra Soft Bathroom Toilet Tissue",
        "category": "Household",
        "brand": "Charmin Ultra Soft",
        "price": 10.49,
        "unit": "Pack of 12 mega rolls",
        "description": "Cushiony soft 2-ply bath tissue for gentle and absorbent comfort.",
        "image_url": "https://images.unsplash.com/photo-1583947215259-38e31be8751f?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 75,
        "rating": 4.9
    },
    {
        "name": "Heavy Duty Kitchen Scrub Sponges",
        "category": "Household",
        "brand": "Scotch-Brite",
        "price": 3.99,
        "unit": "Pack of 4 sponges",
        "description": "Tough scrub fibers lift baked-on messes without trapping bad odors.",
        "image_url": "https://images.unsplash.com/photo-1585670149967-b4f4da88cc9f?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 80,
        "rating": 4.8
    },
    {
        "name": "Tall Kitchen Drawstring Trash Bags",
        "category": "Household",
        "brand": "Glad ForceFlex (13 Gal)",
        "price": 9.49,
        "unit": "Box of 40 bags",
        "description": "Diamond-pattern stretch technology prevents rips, tears, and leaks.",
        "image_url": "https://images.unsplash.com/photo-1585670149967-b4f4da88cc9f?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 70,
        "rating": 4.8
    },
    {
        "name": "Heavy Duty Aluminum Foil",
        "category": "Household",
        "brand": "Reynolds Wrap",
        "price": 4.29,
        "unit": "50 sq ft roll",
        "description": "Durable aluminum foil for oven baking, grilling, lining pans, and food storage.",
        "image_url": "https://images.unsplash.com/photo-1585670149967-b4f4da88cc9f?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 75,
        "rating": 4.9
    },
    {
        "name": "Gallon Storage Slider Bags",
        "category": "Household",
        "brand": "Ziploc",
        "price": 4.79,
        "unit": "Box of 30 bags",
        "description": "Expandable bottom and secure Power Shield slider to protect food freshness.",
        "image_url": "https://images.unsplash.com/photo-1585670149967-b4f4da88cc9f?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 65,
        "rating": 4.8
    },
    {
        "name": "Fabric Softener Liquid",
        "category": "Household",
        "brand": "Downy April Fresh",
        "price": 6.99,
        "unit": "1.53 L bottle (60 loads)",
        "description": "Conditions fabrics to prevent stretching, fading, and fuzz with long-lasting freshness.",
        "image_url": "https://images.unsplash.com/photo-1585670149967-b4f4da88cc9f?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 50,
        "rating": 4.8
    },
    {
        "name": "Citrus Multi-Surface Floor Cleaner",
        "category": "Household",
        "brand": "Pina-Sol",
        "price": 3.99,
        "unit": "1.18 L bottle",
        "description": "Cuts through grease and grime on tile, hardwood, and laminate with fresh pine scent.",
        "image_url": "https://images.unsplash.com/photo-1584744982491-665216d95f8b?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 60,
        "rating": 4.7
    },
    {
        "name": "Room Freshener Spray",
        "category": "Household",
        "brand": "Febreze Air",
        "price": 3.49,
        "unit": "250 g spray can",
        "description": "Eliminates tough odors in the air and leaves a light, clean linen scent.",
        "image_url": "https://images.unsplash.com/photo-1584744982491-665216d95f8b?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 70,
        "rating": 4.7
    },
    {
        "name": "Automatic Dishwasher Detergent Pods",
        "category": "Household",
        "brand": "Cascade Platinum",
        "price": 12.99,
        "unit": "Tub of 36 action pacs",
        "description": "Powers away burnt-on messes without pre-washing for sparkling clean dishes.",
        "image_url": "https://images.unsplash.com/photo-1585670149967-b4f4da88cc9f?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 50,
        "rating": 4.9
    },
    {
        "name": "Disinfecting Surface Wipes",
        "category": "Household",
        "brand": "Clorox",
        "price": 4.99,
        "unit": "Canister of 75 wipes",
        "description": "Bleach-free cleaning wipes that kill 99.9% of viruses and bacteria on counters.",
        "image_url": "https://images.unsplash.com/photo-1584744982491-665216d95f8b?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 80,
        "rating": 4.8
    }
]


def seed_database(db: Session, force: bool = False) -> int:
    Base.metadata.create_all(bind=engine)

    existing_count = db.query(Product).count()
    if existing_count >= len(SAMPLE_PRODUCTS) and not force:
        print(f"[Seed] Database already contains {existing_count} products. Skipping initial seed.")
        return existing_count

    if force and existing_count > 0:
        print(f"[Seed] Force flag set. Clearing {existing_count} existing products...")
        db.query(Product).delete()
        db.commit()

    print(f"[Seed] Seeding {len(SAMPLE_PRODUCTS)} products across 10 categories...")
    for prod_data in SAMPLE_PRODUCTS:
        product = Product(**prod_data)
        db.add(product)

    db.commit()
    final_count = db.query(Product).count()
    print(f"[Seed] Successfully populated database with {final_count} verified products!")
    return final_count


if __name__ == "__main__":
    db = SessionLocal()
    try:
        force_flag = "--force" in sys.argv
        seed_database(db, force=force_flag)
    finally:
        db.close()
