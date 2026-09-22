# Task 02: deposit income
# Asks for deposit amount and annual rate, prints yearly income and total balance.

amount = float(input("Deposit amount: "))
rate = float(input("Interest rate, %: "))

income = amount * rate / 100
total = amount + income

print(f"Income for the year: {income:.2f}")
print(f"Total balance: {total:.2f}")