"""
=============================================================================
  Module 05: Reading Real Code — Practice Exercise
=============================================================================
  This is a REAL code file with bugs. Your job is NOT to fix them yet —
  it's to READ the code and ANSWER QUESTIONS about it.

  This exercise trains you to understand code written by someone else,
  which is the #1 skill you need for Weeks 1-8.

  HOW TO USE:
  1. Read the code below carefully
  2. Answer the questions at the bottom (fill in the functions)
  3. Run tests: python -m pytest test_reading.py -v
=============================================================================
"""

import json
import logging
from datetime import datetime

logger = logging.getLogger("inventory")


# ═══════════════════════════════════════════════════════════════════
# THE CODE TO READ — This is an inventory management system.
# A previous intern wrote it. It has 3 bugs. Don't fix them yet —
# just understand what the code TRIES to do.
# ═══════════════════════════════════════════════════════════════════

class Product:
    """Represents a product in the inventory."""
    
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.created_at = datetime.now()
    
    def __repr__(self):
        return f"Product({self.product_id}, '{self.name}', ${self.price}, qty={self.quantity})"


class InventoryManager:
    """Manages a collection of products."""
    
    def __init__(self):
        self.products = {}          # dict of product_id → Product
        self.transaction_log = []   # list of all changes
    
    def add_product(self, product_id, name, price, quantity):
        """Add a new product or update quantity if it already exists."""
        if product_id in self.products:
            # BUG 1: This should ADD to existing quantity, not replace it
            self.products[product_id].quantity = quantity
            logger.info(f"Updated {name}: qty={quantity}")
        else:
            product = Product(product_id, name, price, quantity)
            self.products[product_id] = product
            logger.info(f"Added new product: {product}")
        
        self.transaction_log.append({
            "action": "add",
            "product_id": product_id,
            "quantity": quantity,
            "timestamp": datetime.now().isoformat()
        })
    
    def remove_product(self, product_id, quantity):
        """Remove a quantity of a product. Returns True if successful."""
        if product_id not in self.products:
            logger.warning(f"Product {product_id} not found")
            return False
        
        product = self.products[product_id]
        
        # BUG 2: Should check if quantity > product.quantity BEFORE removing
        product.quantity -= quantity
        
        if product.quantity < 0:
            logger.error(f"Negative inventory for {product.name}: {product.quantity}")
            product.quantity = 0
            return False
        
        self.transaction_log.append({
            "action": "remove",
            "product_id": product_id,
            "quantity": quantity,
            "timestamp": datetime.now().isoformat()
        })
        
        return True
    
    def get_total_value(self):
        """Calculate total inventory value (price × quantity for all products)."""
        total = 0
        for product in self.products.values():
            # BUG 3: Should be price * quantity, not price + quantity
            total += product.price + product.quantity
        return total
    
    def get_low_stock(self, threshold=5):
        """Return list of products with quantity below threshold."""
        low_stock = []
        for product in self.products.values():
            if product.quantity < threshold:
                low_stock.append(product)
        return low_stock
    
    def export_to_json(self):
        """Export all products as a JSON string."""
        data = []
        for product in self.products.values():
            data.append({
                "id": product.product_id,
                "name": product.name,
                "price": product.price,
                "quantity": product.quantity,
            })
        return json.dumps(data, indent=2)


# ═══════════════════════════════════════════════════════════════════
# YOUR TASK: Answer the questions below by filling in the functions.
# These test your ability to READ and UNDERSTAND the code above.
# Do NOT fix the bugs — just demonstrate that you can find them.
# ═══════════════════════════════════════════════════════════════════


# QUESTION 1: What does the InventoryManager store products in?
# Return the TYPE as a string: "list", "dict", "set", or "tuple"
def answer_storage_type():
    # Look at __init__ in InventoryManager — what type is self.products?
    return None  # TODO: Replace with your answer


# QUESTION 2: What is the bug in add_product?
# Return a string describing the bug in one sentence.
# Hint: Look at what happens when a product_id ALREADY EXISTS
def answer_bug_1():
    # Choose the correct answer:
    # "a" - It doesn't check if price is negative
    # "b" - It replaces quantity instead of adding to it
    # "c" - It doesn't log the transaction
    # "d" - It crashes when product_id is None
    return None  # TODO: Replace with "a", "b", "c", or "d"


# QUESTION 3: What is the bug in remove_product?
# Hint: Think about what happens if you try to remove MORE than what's available
def answer_bug_2():
    # Choose the correct answer:
    # "a" - It doesn't log the transaction
    # "b" - It subtracts before checking if there's enough stock
    # "c" - It doesn't handle negative product IDs
    # "d" - It returns True when it should return False
    return None  # TODO: Replace with "a", "b", "c", or "d"


# QUESTION 4: What is the bug in get_total_value?
# Hint: Math operation is wrong
def answer_bug_3():
    # Choose the correct answer:
    # "a" - It doesn't include products with zero quantity
    # "b" - It uses addition instead of multiplication
    # "c" - It forgets to convert to float
    # "d" - It counts each product twice
    return None  # TODO: Replace with "a", "b", "c", or "d"


# QUESTION 5: If we add Product("P1", "Laptop", 999.99, 10) and
# Product("P2", "Mouse", 29.99, 50), what SHOULD get_total_value() return?
# (Calculate the CORRECT value, not the buggy one)
def answer_correct_total():
    # Correct formula: (999.99 × 10) + (29.99 × 50) = ?
    return None  # TODO: Replace with the correct number


# QUESTION 6: What method would you call to find products with less than
# 3 items in stock? Write the method name as a string.
def answer_low_stock_method():
    return None  # TODO: Replace with the method name (as a string)


# QUESTION 7: How many bugs are in this file?
def answer_bug_count():
    return None  # TODO: Replace with a number


# QUESTION 8: Which line number contains BUG 1?
# (Look at the line that has the actual bug, not the comment)
def answer_bug_1_line():
    # Hint: It's the line that does the wrong thing with quantity
    return None  # TODO: Replace with the line number (an integer)
