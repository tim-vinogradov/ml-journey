# Task 03: loan payment
# Asks for loan amount, term in months and annual rate, prints total interest, total cost and monthly payment.

loan = float(input("Loan amount: "))
term = int(input("Loan term (in months): "))
rate = float(input("Loan rate, % "))

total_interest = loan * rate / 100 * (term/12)
total_cost = loan + total_interest
monthly_payment = total_cost / term

print (f"Total interest: {total_interest:.2f}")
print (f"Total cost: {total_cost:.2f}")
print (f"Monthly payment: {monthly_payment:.2f}")