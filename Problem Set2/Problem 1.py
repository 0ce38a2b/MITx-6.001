'''
To help you get started, here is a rough outline of the stages you should probably follow in writing your code:

For each month:

Compute the monthly payment, based on the previous month’s balance.

Update the outstanding balance by removing the payment, then charging interest on the result.

Output the month, the minimum monthly payment and the remaining balance.

Keep track of the total amount of paid over all the past months so far.

Print out the result statement with the total amount paid and the remaining balance.

A summary of the required math is found below:

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''

balance = 5000
annualInterestRate = 0.18
monthlyPaymentRate = 0.02

previous_balance = balance


def update_balance(previous_balance_):

    def monthly_payment(previous_balance_):
        return monthlyPaymentRate * previous_balance_

    remaining = previous_balance_ - monthly_payment(previous_balance_)
    update_balance_ = round(remaining + annualInterestRate/12*remaining, 2)
    return update_balance_


for i in range(12):
   balance = update_balance(balance)

print(balance)








