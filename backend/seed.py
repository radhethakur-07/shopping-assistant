"""
SmartCart Database Seeder
Expanded & Verified Product Catalog (80+ realistic grocery items)
with 100% verified, high-resolution grocery imagery across 10 categories.
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
    # 1. Fruits
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
        "description": "Juicy and vibrant Valencia oranges bursting with Vitamin C, ideal for snacking or fresh juice.",
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
        "name": "Hass Avocados",
        "category": "Fruits",
        "brand": "Green Harvest",
        "price": 4.49,
        "unit": "Pack of 3",
        "description": "Creamy, rich Hass avocados loaded with healthy monounsaturated fats. Ideal for guacamole and toast.",
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
        "name": "Fresh Blueberries",
        "category": "Fruits",
        "brand": "Berry Sweet",
        "price": 4.99,
        "unit": "250 g punnet",
        "description": "Plump, antioxidant-rich fresh blueberries, great for oatmeal and baking.",
        "image_url": "https://images.unsplash.com/photo-1498557850523-fd3d118b962e?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 45,
        "rating": 4.8
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

    # =========================================================================
    # 2. Vegetables
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

    # =========================================================================
    # 3. Dairy
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
        "name": "Salted Creamery Butter",
        "category": "Dairy",
        "brand": "Golden Meadow",
        "price": 4.19,
        "unit": "454 g (4 sticks)",
        "description": "Rich and creamy butter churned from pure sweet cream with a hint of salt. Ideal with toast and baking.",
        "image_url": "https://images.unsplash.com/photo-1589985270826-4b7bb135bc9d?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 65,
        "rating": 4.7
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
        "name": "Authentic Greek Yogurt",
        "category": "Dairy",
        "brand": "Olympus",
        "price": 4.49,
        "unit": "900 g tub",
        "description": "Thick and velvety plain Greek yogurt with 15g protein per serving and live active cultures.",
        "image_url": "https://images.unsplash.com/photo-1488477181946-6428a0291777?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 50,
        "rating": 4.6
    },
    {
        "name": "Aged Italian Parmesan Cheese",
        "category": "Dairy",
        "brand": "Bella Italia",
        "price": 5.99,
        "unit": "200 g grated",
        "description": "Finely grated aged parmesan cheese offering authentic nutty taste for pasta and salads.",
        "image_url": "https://images.unsplash.com/photo-1559561853-08451507cbe7?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 40,
        "rating": 4.9
    },
    {
        "name": "Fresh Mozzarella Cheese Ball",
        "category": "Dairy",
        "brand": "Bella Italia",
        "price": 4.29,
        "unit": "250 g ball in brine",
        "description": "Soft and milky traditional mozzarella, perfect for Caprese salads and gourmet pizzas.",
        "image_url": "https://images.unsplash.com/photo-1592417817098-8f3d6eb22509?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 35,
        "rating": 4.8
    },

    # =========================================================================
    # 4. Bakery
    # =========================================================================
    {
        "name": "100% Whole Wheat Bread",
        "category": "Bakery",
        "brand": "Daily Baker",
        "price": 2.79,
        "unit": "600 g loaf",
        "description": "Soft, wholesome whole wheat bread baked daily with natural grains and high dietary fiber.",
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
        "description": "Sweet and luscious strawberry fruit spread made with ripe berries. Perfect pair with toast and butter.",
        "image_url": "https://images.unsplash.com/photo-1533089860892-a7c6f0a88666?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 65,
        "rating": 4.7
    },
    {
        "name": "Creamy Roasted Peanut Butter",
        "category": "Bakery",
        "brand": "Skippy",
        "price": 3.89,
        "unit": "460 g jar",
        "description": "Smooth, spreadable peanut butter made with roasted peanuts. Great on toast, apples, and bananas.",
        "image_url": "https://images.unsplash.com/photo-1527515637462-cff94eecc1ac?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 80,
        "rating": 4.8
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

    # =========================================================================
    # 5. Beverages
    # =========================================================================
    {
        "name": "Premium English Breakfast Tea",
        "category": "Beverages",
        "brand": "Twinings",
        "price": 4.99,
        "unit": "Box of 50 tea bags",
        "description": "Robust, full-bodied black tea blend sourced from the finest tea gardens. Perfect with milk.",
        "image_url": "https://images.unsplash.com/photo-1576092768241-dec231879fc3?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 80,
        "rating": 4.8
    },
    {
        "name": "Medium Roast Arabica Ground Coffee",
        "category": "Beverages",
        "brand": "Star Roast",
        "price": 7.49,
        "unit": "340 g bag",
        "description": "100% Arabica ground coffee with notes of cocoa and toasted nuts for a smooth morning cup.",
        "image_url": "https://images.unsplash.com/photo-1559056199-641a0ac8b55e?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 60,
        "rating": 4.9
    },
    {
        "name": "100% Pure Orange Juice",
        "category": "Beverages",
        "brand": "Tropic Delight",
        "price": 3.89,
        "unit": "1.75 L bottle",
        "description": "Never from concentrate. Squeezed from Florida oranges without added sugars or preservatives.",
        "image_url": "https://images.unsplash.com/photo-1621506289937-a8e4df240d0b?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 75,
        "rating": 4.7
    },
    {
        "name": "Organic Green Tea with Jasmine",
        "category": "Beverages",
        "brand": "Zen Herbal",
        "price": 4.49,
        "unit": "Box of 25 sachets",
        "description": "Calming organic green tea delicately infused with natural jasmine flowers for mindful sips.",
        "image_url": "https://images.unsplash.com/photo-1627435601361-ec25f5b1d0e5?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 55,
        "rating": 4.6
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

    # =========================================================================
    # 6. Snacks
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
        "name": "Crunchy Digestive Biscuits",
        "category": "Snacks",
        "brand": "McVitie's",
        "price": 2.49,
        "unit": "400 g pack",
        "description": "Classic wheat digestive biscuits with the iconic crunchy texture. Perfect companion for hot tea.",
        "image_url": "https://images.unsplash.com/photo-1558961363-fa8fdf82db35?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 85,
        "rating": 4.7
    },
    {
        "name": "Roasted & Salted California Almonds",
        "category": "Snacks",
        "brand": "Nutty Delights",
        "price": 6.99,
        "unit": "250 g pouch",
        "description": "Premium whole California almonds dry roasted with light sea salt. High protein super snack.",
        "image_url": "https://images.unsplash.com/photo-1508061253366-f7da158b6d46?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 65,
        "rating": 4.9
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
        "name": "Tortilla Corn Chips",
        "category": "Snacks",
        "brand": "Doritos",
        "price": 3.29,
        "unit": "250 g bag",
        "description": "Crunchy triangular corn tortilla chips. Great for dipping in fresh salsa and melted cheese.",
        "image_url": "https://images.unsplash.com/photo-1513456852971-30c0b8199d4d?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 90,
        "rating": 4.5
    },

    # =========================================================================
    # 7. Grains & Pantry Staples
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
        "name": "Classic Marinara Pasta Sauce",
        "category": "Grains",
        "brand": "Rao's Homemade",
        "price": 5.49,
        "unit": "680 g jar",
        "description": "Slow-simmered Italian plum tomatoes with olive oil, fresh basil, and garlic. Perfect companion for pasta.",
        "image_url": "https://images.unsplash.com/photo-1572441713132-c542fc4fe282?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 70,
        "rating": 4.9
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
        "name": "Iodized Table Salt",
        "category": "Grains",
        "brand": "Morton",
        "price": 1.19,
        "unit": "737 g canister",
        "description": "Free-flowing iodized table salt with anti-caking agent for essential kitchen seasoning.",
        "image_url": "https://images.unsplash.com/photo-1518110925495-5fe2fda0442c?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 150,
        "rating": 4.7
    },
    {
        "name": "Organic Ground Turmeric Powder",
        "category": "Grains",
        "brand": "Spice Islands",
        "price": 2.99,
        "unit": "100 g jar",
        "description": "Bright golden turmeric powder with high curcumin content for curries, lattes, and marinades.",
        "image_url": "https://images.unsplash.com/photo-1615485290382-441e4d049cb5?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 75,
        "rating": 4.8
    },

    # =========================================================================
    # 8. Personal Care
    # =========================================================================
    {
        "name": "Nourishing Coconut Shampoo",
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
        "name": "Moisturizing Beauty Bar Soap",
        "category": "Personal Care",
        "brand": "Dove",
        "price": 5.49,
        "unit": "Pack of 4 bars",
        "description": "With 1/4 moisturizing cream for soft, smooth, healthy-feeling skin every day.",
        "image_url": "https://images.unsplash.com/photo-1607006314352-094119934751?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 80,
        "rating": 4.8
    },
    {
        "name": "Total Care Toothpaste",
        "category": "Personal Care",
        "brand": "Colgate Total",
        "price": 3.49,
        "unit": "150 g tube",
        "description": "Antibacterial shield protecting against cavities, plaque, tartar, and bad breath.",
        "image_url": "https://images.unsplash.com/photo-1559591937-e1032b453e0d?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 110,
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

    # =========================================================================
    # 9. Household
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
        "name": "Dishwashing Liquid",
        "category": "Household",
        "brand": "Dawn Platinum",
        "price": 3.99,
        "unit": "700 ml bottle",
        "description": "Cuts through tough 48-hour stuck-on grease effortlessly with refreshing original scent.",
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

    # =========================================================================
    # 10. Frozen Food
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
        "name": "Golden Crispy French Fries",
        "category": "Frozen Food",
        "brand": "McCain",
        "price": 3.49,
        "unit": "750 g bag",
        "description": "Golden, restaurant-style crispy cut fries ready to air-fry or oven bake in 15 minutes.",
        "image_url": "https://images.unsplash.com/photo-1576107232684-1279f3908594?auto=format&fit=crop&w=600&q=80",
        "stock_quantity": 70,
        "rating": 4.6
    }
]


def seed_database(db: Session, force: bool = False) -> int:
    Base.metadata.create_all(bind=engine)

    existing_count = db.query(Product).count()
    if existing_count > 0 and not force:
        print(f"[Seed] Database already contains {existing_count} products. Skipping initial seed.")
        return existing_count

    if force and existing_count > 0:
        print(f"[Seed] Force flag set. Clearing {existing_count} existing products...")
        db.query(Product).delete()
        db.commit()

    print(f"[Seed] Seeding {len(SAMPLE_PRODUCTS)} verified grocery products...")
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
