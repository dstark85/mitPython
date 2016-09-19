# This program runs through a calculation of interest rate by month

def compound(charge, apr):
    '''
    Charge is a float that represents the amount charged to credit card
    apr is a float also representing a percentage (0.1 = 10%)
    Uses bisection to find the fixed amount
    Returns the minimum fixed amount to pay off the the debt
    '''
    def calc_interest(amount, apr):
        '''
        Takes amount, apr as floats and returns the amount of interest
            accrued       
        '''
        return 	apr / 12 * amount
 
    min_amount = charge // 12  # slight optimization
    max_amount = (charge * (1 + apr) ** 12) / 12
    fixed_monthly_payment = (min_amount + max_amount) / 2

    while True:
        new_balance = charge  

        for i in range(12):
            unpaid_balance = new_balance - fixed_monthly_payment 
            interest = calc_interest(unpaid_balance, apr)
            new_balance = unpaid_balance + interest

        if new_balance < 0: # sufficient money paid
            if abs(new_balance) < 0.01:  # when less than a cent
                return round(fixed_monthly_payment, 2)
            max_amount = fixed_monthly_payment 
        elif new_balance > 0: # not enough money paid monthly 
            min_amount = fixed_monthly_payment 
        fixed_monthly_payment = (max_amount + min_amount) / 2

print("Test case 1 ", compound(320000, 0.2))
print("Test case 2 ", compound(999999, 0.18))
