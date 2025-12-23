class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance   

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Nạp {amount} vào tài khoản. Số dư hiện tại: {self.__balance}")
        else:
            print("Số tiền nạp phải lớn hơn 0.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Rút {amount} từ tài khoản. Số dư hiện tại: {self.__balance}")
        else:
            print("Số tiền rút không hợp lệ hoặc vượt quá số dư.")

    def get_balance(self):
        return self.__balance
account = BankAccount("Giang", 1000)

account.deposit(500)
account.withdraw(300)
print("Số dư cuối cùng:", account.get_balance())

