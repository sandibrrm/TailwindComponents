# test_tailwindcomponents.py
"""
Tests for TailwindComponents module.
"""

import unittest
from tailwindcomponents import TailwindComponents

class TestTailwindComponents(unittest.TestCase):
    """Test cases for TailwindComponents class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TailwindComponents()
        self.assertIsInstance(instance, TailwindComponents)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TailwindComponents()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
