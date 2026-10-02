# Procedural:

balance = 1000

def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    return balance - amount

balance = deposit(balance, 200)
balance = withdraw(balance, 50)

# works fine for a single account and a couple of operations
# but once you have multiple accounts
alice_balance = 1000
bob_balance = 500

alice_balance = deposit(alice_balance, 200)
alice_interest_rate = 3
bob_balance = withdraw(bob_balance, 50)
bobs_interest_rate = 4
# you start having to manually keep the right data connected to the right operations


# OOP
class BankAccount:
    def __init__(self, owner, balance):
        self._owner = owner
        self._balance = balance
        self._interest_rate = 3.0

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def apply_interest(self):
        pass

alice = BankAccount("Alice", 1000)
bob = BankAccount("Bob", 500)

alice.deposit(200)
bob.withdraw(50)

# Here OOP becomes useful because each account owns its own state.


# What about when procedural programming would be better? 

# Converting a temperature
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

print(fahrenheit_to_celsius(72))

# Making that OOP
class TemperatureConverter:
    def fahrenheit_to_celsius(self, f):
        return (f - 32) * 5 / 9

converter = TemperatureConverter()
print(converter.fahrenheit_to_celsius(72))

# doesn't add anything, mostly just extra ceremony to your function

# Concise rule:
# Procedural programming works well when the problem is primarily a sequence of steps.
# OOP works well when the problem is primarily about multiple things that have their own data and behavior.

# Lastly, real programs often mix both: objects for the major entities, procedural/helper functions for straightforward calculations or workflows.