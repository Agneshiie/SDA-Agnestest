"""
ATM Pin Verification
Problem:
Create an ATM Pin Verification System where the user must enter the correct PIN to access their account. The correct PIN is 1234.

Criteria:
The user has up to 3 attempts to enter the correct PIN.
If the PIN is correct, print "PIN verified successfully! Access granted."
If the PIN is incorrect, print how many attempts are left.
After 3 incorrect attempts, lock the user out and print "Incorrect PIN. You have been locked out."
Ensure the program only accepts numeric input for the PIN.

Steps:
Prompt the user to enter their PIN.
Check if the entered PIN matches 1234.
Provide feedback on the remaining attempts.
Lock the user out after 3 failed attempts.
"""

def atm_pin_verification():
    correct_pin = "1234"
    attempts = 0
    max_attempts = 3

    print("Welcome to the ATM!")

    while attempts < max_attempts:
        entered_pin = input("Enter your PIN: ")
        attempts += 1

        if entered_pin == correct_pin:
            print("PIN verified successfully! Access granted")
            break
        else:
            if attempts < max_attempts:
                print(f"Incorrect PIN. You have {max_attempts - attempts} attempt(s) left.")
            else:
                print("Incorrect PIN. You have been locked out!")
                break

#atm_pin_verification()


def atm_pin_verification():
    correct_pin = "1234"
    max_attempts = 3

    print("Welcome to the ATM!")

    for attempt in range(1, max_attempts + 1):
        entered_pin = input("Enter yout PIN: ")

        if entered_pin == correct_pin:
            print("PIN verified successfully! Access granted")
            return
        else:
            remaining_attempts = max_attempts - attempt
            if remaining_attempts > 0:
                print(f"incorrect PIN. You have {remaining_attempts} attempt(s) left.")
            else:
                print("Incorrect PIN. You have been locked out")

#atm_pin_verification()

"""
Create an ATM System that verifies the user's PIN and provides options to check balance, deposit money, or withdraw money. The system should handle incorrect PIN attempts and balance checks.

Criteria:
PIN Verification:

The user has 3 attempts to enter the correct PIN (1234).
After 3 incorrect attempts, lock the user out.
Menu Options:

After a correct PIN, the user should see the menu with 4 options:
Check balance: Show the current balance.
Deposit money: Allow the user to deposit money into their account.
Withdraw money: Allow the user to withdraw money if they have enough balance.
Exit: Exit the ATM system.
Transaction Validation:

Ensure that the withdrawal amount doesn't exceed the balance.
Deposit and withdrawal amounts should be numeric.
Edge Cases:

Handle invalid choices in the menu and prompt the user again.
Ensure only numeric input is allowed for deposit and withdrawal amounts.

Steps:
Prompt the user to enter their PIN.
Check if the entered PIN is correct, and allow access if it is.
Show the menu with options to check balance, deposit, withdraw, or exit.
Allow the user to deposit or withdraw money, and update the balance accordingly.
Handle invalid inputs and ensure sufficient funds for withdrawals.
"""

def atm_system():
    pin = "1234"
    balance = 570
    attempts = 3
    currency = "€"

    print("Welcome to the ATM system!")

    while attempts > 0:
        entered_pin = input("Please enter your pin: ")

        if entered_pin == pin:
            print("PIN accepted. Welcome")
            break
        else:
            attempts -= 1
            print(f"Incorrect pin. You have {attempts} attempts left.")
            if attempts == 0:
                print("You have been locked out of the ATM")
                return
            
    while True:
        print("\nMenu:") #uus rida enne menüüpunkte
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. End session")

        choice = input("Please choose an option (1-4): ")

        if choice == "1":
            print(f"Your current balance is {balance}{currency}.")
        elif choice == "2":
            deposit_amount = float(input(f"Enter deposit amount {currency}: "))
            balance += deposit_amount
            print(f"You have successfully deposited {deposit_amount}{currency}. New balance: {balance}{currency}.")
        elif choice == "3":
            withdraw_amount = float(input(f"Enter withdrawal amount {currency}: "))
            if withdraw_amount > balance:
                print("Insufficient funds.")
            else:
                balance -= withdraw_amount
                print(f"You have successfully withdrawn {withdraw_amount}{currency}. New balance: {balance}{currency}.")
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

atm_system()