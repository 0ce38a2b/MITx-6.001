'''
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months.
By a fixed monthly payment, we mean a single number which does not change each month,
but instead is a constant amount that will be paid each month.

Start with $10 payments per month and calculate whether the balance will be paid off in a year this way
(be sure to take into account the interest accrued each month).
If $10 monthly payments are insufficient to pay off the debt within a year, increase the monthly payment by $10 and repeat.
'''
balance = 50000
annualInterestRate = 0.18

init_balance = balance
month_interest_rate = annualInterestRate / 12.0
monthly_payment = 0

while(True):
    for i in range(12):
        Monthly_unpaid_balance = balance - monthly_payment
        balance = Monthly_unpaid_balance + (Monthly_unpaid_balance * month_interest_rate)

    if(balance >= 0):
        monthly_payment += 10
        balance = init_balance    # !!!
    else:
        break

print(monthly_payment)






















