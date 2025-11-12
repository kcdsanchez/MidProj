# This is the artifact for Topic 3: Integrated Testing (The Test File)
import unittest
from topic3_logic import Calculator

# This test will pass
def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0

# This test will pass
def test_subtract():
    calc = Calculator()
    assert calc.subtract(10, 5) == 5
    assert calc.subtract(2, 1) == 1


# This test will FAIL, then PASS after the fix
def test_divide_by_zero_fails_demo():
    calc = Calculator()
    # STEP 4: Show this test failing (Expected: "Error", Actual: None)
    # STEP 6: Re-run this single test to show it passes
    assert calc.divide(10, 0) == "Error"
