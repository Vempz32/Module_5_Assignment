"""
Description: Chatbot application.  Allows user to perform balance 
inquiries and make deposits to their accounts.
Author: ACE Department
Modified by: {Student Name}
Date: 2023-10-15
Usage: From the console: python src/chatbot.py
"""

## GIVEN CONSTANT COLLECTIONS
ACCOUNTS = {
    123456 : {"balance" : 1000.0},
    789012 : {"balance" : 2000.0}
}

VALID_TASKS = {"balance", "deposit", "exit"}

## CODE REQUIRED FUNCTIONS STARTING HERE:
def get_account() -> int:
    """
    Prompts the user to enter their account number and checks if it's valid.
    Returns the account number if valid, otherwise returns None.
    Raises ValueError for invalid inputs.
    """
    try:
        account_number = input("Please enter your account number: ")
        
        # Check if the input is a digit (whole number)
        if not account_number.isdigit():
            raise ValueError("Account number must be a whole number.")
        
        # Convert the account number to an integer
        account_number = int(account_number)
        
        # Check if the account number exists in the ACCOUNTS dictionary
        if account_number in ACCOUNTS:
            return account_number
        else:
            raise ValueError("Account number entered does not exist.")
    
    except ValueError as e:
        print(e)
        return None
def get_amount() -> float:
    """
    Prompts the user to enter a transaction amount, validates it, and returns it as a float.
    
    Raises:
        ValueError: If the amount is non-numeric or negative.
    """
    try:
        transaction_amount =  input("Please enter the transaction amount: ")
        if transaction_amount > 0 :
            return
        if transaction_amount.isnumeric():
            raise ValueError("Invalid Amount. Amount must be numeric")
        if transaction_amount <  0 :
            raise ValueError("Invalid amount. Please enter a positive number.")
    except ValueError as e:
        print(e)
        return None  # Return None to indicate failure

        
    


## GIVEN CHATBOT FUNCTION
get_account()
## REQUIRES REVISION
"""
def chatbot():
    '''
    The main program.  Uses the functionality of the functions:
        get_account()
        get_amount()
        get_balance()
        make_deposit()
        user_selection()
    '''

    print("Welcome! I'm the PiXELL River Financial Chatbot!  Let's get chatting!")

    keep_going = True
    while keep_going:
        try:
            ## CALL THE user_selection FUNCTION HERE 
            ## CAPTURING THE RESULTS IN A VARIABLE CALLED
            ## selection:

            if selection != "exit":
                
                # Account number validation.
                valid_account = False
                while valid_account == False:
                    try:
                        ## CALL THE get_account FUNCTION HERE
                        ## CAPTURING THE RESULTS IN A VARIABLE 
                        ## CALLED account:

                        valid_account = True
                    except ValueError as e:
                        # Invalid account.
                        print(e)
                if selection == "balance":
                        ## CALL THE get_balance FUNCTION HERE
                        ## PASSING THE account VARIABLE DEFINED 
                        ## ABOVE, AND PRINT THE RESULTS:

                else:

                    # Amount validation.
                    valid_amount = False
                    while valid_amount == False:
                        try:
                            ## CALL THE get_amount FUNCTION HERE
                            ## AND CAPTURE THE RESULTS IN A VARIABLE 
                            ## CALLED amount:


                            valid_amount = True
                        except ValueError as e:
                            # Invalid amount.
                            print(e)
                ## CALL THE make_deposit FUNCTION HERE PASSING THE 
                ## VARIABLES account AND amount DEFINED ABOVE AND 
                ## PRINT THE RESULTS:


            else:
                # User selected 'exit'
                keep_going = False
        except ValueError as e:
            # Invalid selection:
            print(e)

    print("Thank you for banking with PiXELL River Financial.")
"""
    
"""
if __name__ == "__main__":
    chatbot()
"""
