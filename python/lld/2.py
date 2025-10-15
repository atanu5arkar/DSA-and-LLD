"""
Encapsulation limits outside interference to the state of an object by allowing
declaration of private attributes.

The class must define methods, aptly called Setters and Getters, for the outside
world to read or mutate private variables.

The primary advantage: more maintainable code.
"""


class BankAccount:
    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.__balance = balance

    # getter
    def curr_balance(self):
        return self.__balance

    # setter
    def credit(self, amount: float):
        if amount < 10:
            return print("This is below me!")

        self.__balance += amount
        return print(f"Your account is credited with INR {amount}")


account = BankAccount("Atanu", 45.72)

# Error
# print(account.__balance)

account.credit(45.89)
account.credit(0.02)

print("Current Balance:", account.curr_balance())
