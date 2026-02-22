"""
Tests for Module 05: Reading Real Code
Run with: python -m pytest test_reading.py -v
"""
import pytest
from starter import (
    answer_storage_type,
    answer_bug_1,
    answer_bug_2,
    answer_bug_3,
    answer_correct_total,
    answer_low_stock_method,
    answer_bug_count,
    answer_bug_1_line,
)


class TestCodeReading:
    def test_q1_storage_type(self):
        assert answer_storage_type() == "dict", "Products are stored in a dictionary (dict)"

    def test_q2_bug_1(self):
        assert answer_bug_1() == "b", "Bug 1: quantity is REPLACED instead of ADDED to"

    def test_q3_bug_2(self):
        assert answer_bug_2() == "b", "Bug 2: subtracts BEFORE checking if enough stock"

    def test_q4_bug_3(self):
        assert answer_bug_3() == "b", "Bug 3: uses + instead of * in total calculation"

    def test_q5_correct_total(self):
        expected = (999.99 * 10) + (29.99 * 50)
        result = answer_correct_total()
        assert result is not None, "Please calculate the correct total"
        assert abs(result - expected) < 0.01, f"Expected {expected}, got {result}"

    def test_q6_low_stock_method(self):
        answer = answer_low_stock_method()
        assert answer is not None, "Please provide the method name"
        assert "low_stock" in answer.lower(), "The method name contains 'low_stock'"

    def test_q7_bug_count(self):
        assert answer_bug_count() == 3, "There are exactly 3 bugs marked in the code"

    def test_q8_bug_1_line(self):
        result = answer_bug_1_line()
        assert result is not None, "Please provide the line number"
        # BUG 1 is on the line: self.products[product_id].quantity = quantity
        # Allow some flexibility since line numbers may shift slightly
        assert 55 <= result <= 60, f"Bug 1 is around line 57 (got {result})"
