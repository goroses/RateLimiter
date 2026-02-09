# test_ratelimiter.py
"""
Tests for RateLimiter module.
"""

import unittest
from ratelimiter import RateLimiter

class TestRateLimiter(unittest.TestCase):
    """Test cases for RateLimiter class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RateLimiter()
        self.assertIsInstance(instance, RateLimiter)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RateLimiter()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
