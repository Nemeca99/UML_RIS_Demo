"""
UML Calculator - Community Edition Tests
"""
import unittest
import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.ris_community import ris
from core.symbolic import evaluate_expression, solve_equation

class TestRisCommunity(unittest.TestCase):
    """Test cases for RIS Community Edition"""
    
    def test_basic_operations(self):
        """Test basic RIS operations"""
        # Equal values
        self.assertEqual(ris(5, 5), 25)
        
        # Zero values
        self.assertEqual(ris(0, 5), 5)
        self.assertEqual(ris(5, 0), 5)
        
        # Divisible values
        self.assertEqual(ris(10, 5), 2)
        
        # Special case
        self.assertEqual(ris(9, 2), 18)  # 9 is divisible by 3
        
        # Default case
        self.assertEqual(ris(7, 4), 11)

class TestSymbolic(unittest.TestCase):
    """Test cases for symbolic calculations"""
    
    def test_expression_evaluation(self):
        """Test expression evaluation"""
        self.assertAlmostEqual(evaluate_expression("2 + 3*5"), 17.0)
        self.assertAlmostEqual(evaluate_expression("3^2 - 4"), 5.0)
        
    def test_equation_solving(self):
        """Test equation solving"""
        solutions = solve_equation("x^2 - 4 = 0")
        if isinstance(solutions, list):
            self.assertEqual(set([float(s) for s in solutions]), {-2.0, 2.0})
        else:
            self.fail("Expected list of solutions")

if __name__ == "__main__":
    unittest.main()
