# This program runs through a calculation of interest rate by month

def compound(charge, min_payment, apr):
    '''
    Charge is a float that represents the amount charged to credit card
    min_payment is a float representing a percentage (0.1 = 10%)
    apr is a float also representing a percentage (0.1 = 10%)
    Calculates the new balance for each month
    return the balance after one year of minimum payments.
       Can consider how long the debt would take to get rid of.
    ans -- The debt will never be paid off ---
    '''
    def calc_interest(amount, apr):
        '''
        Takes amount, apr as floats and returns the amount of interest
            accrued       
        '''
        return 	apr / 12 * amount
 
    new_balance = charge  
    total_paid = 0

    months = 0
    while new_balance > 1:  # quit when debt is below a dollar
        payment = new_balance * min_payment
        total_paid += payment
        unpaid_balance = new_balance - payment
        interest = calc_interest(unpaid_balance, apr)
        new_balance = unpaid_balance + interest
        months += 1
        print(new_balance)

    return months 


months = compound(5000, .12, .18)
print("The total number of months to pay off the debt:", months)
