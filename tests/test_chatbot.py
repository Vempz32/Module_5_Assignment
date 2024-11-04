"""
Description: Unit tests for the chatbot application.
Author: 
Date:
Usage: Run this file to execute unit tests for chatbot functions.
"""

import unittest
from unittest.mock import patch
from src.chatbot import get_account, get_amount, ACCOUNTS
from src.chatbot import get_balance, ACCOUNTS
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
    

class TestGetBalance(unittest.TestCase):
    def test_valid_balance(self):
        # Arrange
        account = 123456  # Valid account number
        expected_message = 'Your current balance for account 123456 is $1,000.00.'  # Expected output

        # Act
        result = get_balance(account)  # Call the function

        # Assert
        self.assertEqual(result, expected_message)  # Verify the result matches expected output

    def test_account_not_exist(self):
        # Arrange
        account = 112233  # Non-existent account number
        
        # Act & Assert
        with self.assertRaises(ValueError) as context:
            get_balance(account)  # Call the function which should raise ValueError

        # Verify that the correct message is included in the raised exception
        self.assertEqual(str(context.exception), "Account number does not exist.")


                



    

