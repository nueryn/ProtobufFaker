# test_protobuffaker.py
"""
Tests for ProtobufFaker module.
"""

import unittest
from protobuffaker import ProtobufFaker

class TestProtobufFaker(unittest.TestCase):
    """Test cases for ProtobufFaker class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ProtobufFaker()
        self.assertIsInstance(instance, ProtobufFaker)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ProtobufFaker()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
