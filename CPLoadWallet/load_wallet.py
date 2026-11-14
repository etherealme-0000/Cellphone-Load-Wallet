class LoadWallet:
    SERVICE_FEE = 5.00 

    def __init__(self, owner_name, mobile_number, starting_balance=0.0):
        self.owner_name = owner_name
        self.mobile_number = mobile_number
        self.__balance = round(starting_balance, 2)  

    @property
    def balance(self):
        return self.__balance

    def top_up(self, amount):
        if amount <= 0:
            print("Top-up rejected: amount must be greater than zero.")
            return False
        self.__balance = round(self.__balance + amount, 2)
        print(f"New balance: P{self.__balance:.2f}")
        return True

    def send_load(self, amount, recipient_number):
        return self._send(amount, recipient_number, fee=0.0)

    def send_with_fee(self, amount, recipient_number):
        return self._send(amount, recipient_number, fee=self.SERVICE_FEE)

    def _send(self, amount, recipient_number, fee):
        if amount <= 0:
            print("Transfer rejected: amount must be greater than zero.")
            return False
        if recipient_number == self.mobile_number:
            print("Transfer rejected: you cannot send load to your own number.")
            return False
        total = amount + fee
        if total > self.__balance:
            print(f"Transfer rejected: insufficient balance. "
                  f"Needed P{total:.2f}, available P{self.__balance:.2f}.")
            return False
        self.__balance = round(self.__balance - total, 2)
        if fee > 0:
            print(f"Sent P{amount:.2f} to {recipient_number} (fee P{fee:.2f}).")
        else:
            print(f"Sent P{amount:.2f} to {recipient_number}.")
        print(f"New balance: P{self.__balance:.2f}")
        return True

    def show_balance(self):
       
        print(f"Owner         : {self.owner_name}")
        print(f"Mobile Number : {self.mobile_number}")
        print(f"Balance       : P{self.__balance:.2f}")