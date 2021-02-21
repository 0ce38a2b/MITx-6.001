balance = 320000
annualInterestRate = 0.2

init_balance = balance
month_interest_rate = annualInterestRate / 12.0

lower = init_balance / 12.0
upper = (init_balance*(1+month_interest_rate)**12) / 12.0
monthly_payment = (lower + upper) / 2.0

while(True):
    balance = init_balance
    for i in range(12):
        Monthly_unpaid_balance = balance - monthly_payment
        balance = Monthly_unpaid_balance + (Monthly_unpaid_balance * month_interest_rate)
    balance = float("%.2f" % balance)                  # !!!

    if(balance > 0):
        lower = monthly_payment
        monthly_payment = (lower + upper) / 2.0

    elif(balance < 0):
        upper = monthly_payment
        monthly_payment = (lower + upper) / 2.0

    elif(balance == 0):
        break



print(float("%.2f" % monthly_payment))
