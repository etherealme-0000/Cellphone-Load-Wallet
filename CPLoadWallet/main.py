import math
import os
import sys


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from load_wallet import LoadWallet

MENU = """
MENU
1. Top Up Load
2. Send Load (same network)
3. Send Load (other network, with fee)
4. Show Balance
5. Exit
"""


def read_name(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Name cannot be empty. Please try again.")


def read_mobile(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit() and len(value) == 11 and value.startswith("09"):
            return value
        print("Invalid number. Use 11 digits starting with 09 (e.g. 09171234567).")


def read_amount(prompt, allow_zero=False):
    while True:
        raw = input(prompt).strip().upper().replace("P", "").replace("₱", "").replace(",", "")
        try:
            value = float(raw)
        except ValueError:
            print("Invalid amount. Please enter a number (e.g. 50 or P50).")
            continue
        if not math.isfinite(value) or value < 0 or (value == 0 and not allow_zero):
            print("Amount must be greater than zero." if not allow_zero
                  else "Amount cannot be negative.")
            continue
        return round(value, 2)


def main():
    try:
        owner = read_name("Enter owner name: ")
        number = read_mobile("Enter mobile number: ")
        start = read_amount("Enter starting balance: ", allow_zero=True)
        wallet = LoadWallet(owner, number, start)

        while True:
            print(MENU)
            choice = input("Choose an option (1-5): ").strip()

            if choice == "1":
                wallet.top_up(read_amount("Enter top-up amount: "))
            elif choice == "2":
                target = read_mobile("Enter recipient number: ")
                wallet.send_load(read_amount("Enter amount to send: "), target)
            elif choice == "3":
                target = read_mobile("Enter recipient number: ")
                print(f"A service fee of P{LoadWallet.SERVICE_FEE:.2f} will be added.")
                wallet.send_with_fee(read_amount("Enter amount to send: "), target)
            elif choice == "4":
                wallet.show_balance()
            elif choice == "5":
                print("Thank you for using Load Wallet. Goodbye!")
                break
            else:
                print("Invalid option. Please choose a number from 1 to 5.")
    except (EOFError, KeyboardInterrupt):
        print("\nExiting. Goodbye!")


if __name__ == "__main__":
    main()