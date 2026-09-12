# another simple ATM program, but with better structure and more features lol
# still haven't mastered exceptions so yea.
# I learned about len() and how to use it to check the length of a string, which is pretty useful for validating user input.

def check_balance(balance):
    print(f"Your current balance is: ${balance}\n")
    return balance

def withdraw(balance):
    amount = int(input("Enter withdrawal amount: $"))
    if amount > balance:
        print("Insufficient funds!\n")
    else:
        balance -= amount
        print(f"Successfully withdrew ${amount}. New balance: ${balance}\n")
    return balance

def run_atm_session():
    print("--- Welcome to the Bank ATM ---")

    actions = {
        "1": check_balance,
        "2": withdraw
    }

    balance = 500

    # Main Menu Loop
    while True:
        print("Menu: 1) Check Balance  2) Withdraw  3) Exit")
        choice = input("Choose an option: ").strip()

        if choice == "3":
            print("Thank you for using the ATM. Goodbye!")
            return balance

        action = actions.get(choice)

        if action:
            balance = action(balance)
        else:
            print("Invalid choice. Please pick 1, 2, or 3.\n")


if __name__ == "__main__":
    final_balance = run_atm_session()
    print(f"ATM Session closed. User left with: ${final_balance}")

# lol pretty cool, imma try do more features in the future like deposits, transfers, and maybe even a simple login system.
