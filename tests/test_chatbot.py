"""
Description:
Author:
Date:
Usage:
"""

import unittest
from unittest.mock import patch

from src.chatbot import get_account
from src.chatbot import VALID_TASKS, ACCOUNTS

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


if __name__ == "__main__":
    unittest.main()