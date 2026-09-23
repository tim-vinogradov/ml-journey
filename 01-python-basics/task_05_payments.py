payments = [12000, 12000, 0, 12000, 6000, 12000]
due = 12000
month = 0
missed = 0
partial = 0
average = sum(payments) / len(payments)     

for payment in payments:
    month += 1

    if payment == 0:
        status = "Missed"
        missed += 1
    elif payment < due:
        status = "Partial"
        partial += 1
    else:
        status = "Ok"

    print(f"Month {month}: {payment} - {status}")
print()
print(f"Total paid: {sum(payments)}")
print(f"Average payment: {average:.2f}")
print(f"Missed payments: {missed}")
print(f"Partial payments: {partial}")