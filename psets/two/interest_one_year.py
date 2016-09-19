# This program runs through a calculation of interest rate by month

def compound(charge, apr):
    '''
    Charge is a float that represents the amount charged to credit card
    apr is a float also representing a percentage (0.1 = 10%)
    monthly amount is a multiple of 10
    Returns the minimum fixed amount to pay off the the debt
    '''
    def calc_interest(amount, apr):
        '''
        Takes amount, apr as floats and returns the amount of interest
            accrued       
        '''
        return 	apr / 12 * amount
 
    fixed_monthly_payment = charge // 12  # slight optimization
    fixed_monthly_payment = round(fixed_monthly_payment, -1) # round to tens
    while True:
        new_balance = charge  

        for i in range(12):
            unpaid_balance = new_balance - fixed_monthly_payment 
            interest = calc_interest(unpaid_balance, apr)
            new_balance = unpaid_balance + interest

        if new_balance <= 0:
            return fixed_monthly_payment
        fixed_monthly_payment += 10

print("Minimum fixed monthly payment is:", compound(5000, 0.18))
print("test case 1: ", compound(3329, .2))
print("test case 2: ", compound(4773, .2))
print("test case 3: ", compound(3926, .2))
