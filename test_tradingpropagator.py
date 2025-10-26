# test_tradingpropagator.py
"""
Tests for TradingPropagator module.
"""

import unittest
from tradingpropagator import TradingPropagator

class TestTradingPropagator(unittest.TestCase):
    """Test cases for TradingPropagator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TradingPropagator()
        self.assertIsInstance(instance, TradingPropagator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TradingPropagator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
