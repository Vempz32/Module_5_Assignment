"""
Description: Unit tests for the chatbot application.
Author: 
Date:
Usage: Run this file to execute unit tests for chatbot functions.
"""

import unittest
from unittest.mock import patch
from src.chatbot import get_account, get_amount, ACCOUNTS

class TestGetAccount(unittest.TestCase):
    @patch("builtins.input")
    def test_valid_account_number(self, mock_input):
        # Arrange
        mock_input.side_effect = ["123456"]
        
        # Act
        account = get_account()
        
        # Assert
        self.assertEqual(account, 123456)

    @patch("builtins.input")
    def test_nonexistent_account_number(self, mock_input):
        # Arrange
        mock_input.side_effect = ["112233"]
        
        # Act
        account = get_account()
        
        # Assert
        self.assertIsNone(account)  # Expecting None as the account doesn't exist

    @patch("builtins.input")
    def test_invalid_account_number_format(self, mock_input):
        # Arrange
        mock_input.side_effect = ["alv"]
        
        # Act
        account = get_account()
        
        # Assert
        self.assertIsNone(account)  # Expecting None due to invalid format


class TestGetAmount(unittest.TestCase):
    @patch("builtins.input")
    def test_valid_amount(self, mock_input):
        # Arrange
        mock_input.side_effect = ["500.1"]
        
        # Act
        amount = get_amount()
        
        # Assert
        self.assertEqual(amount, 500.1)

    @patch("builtins.input")
    def test_nonnumeric_amount(self, mock_input):
        # Arrange
        mock_input.side_effect = ["non_numeric_data"]
        
        # Act
        amount = get_amount()
        
        # Assert
        self.assertIsNone(amount) 

    @patch("builtins.input")
    def test_empty_amount(self, mock_input):
        # Arrange
        mock_input.side_effect = ["0"]
        
        # Act
        amount = get_amount()
        
        # Assert
        self.assertEqual(amount, 0.0)  # Expecting 0.0 as valid input


if __name__ == "__main__":
    unittest.main()


