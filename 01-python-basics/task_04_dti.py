monthly_income = int(input("Your monthly income is: "))
monthly_payment = int(input("Your monthly payment is: "))

debt_burden = monthly_payment/monthly_income * 100
if debt_burden > 50:
    print ("High risk")
else:
    print ("Acceptable")

print (f"Your debt burden is: {debt_burden:.1f}%")
