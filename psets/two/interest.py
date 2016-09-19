# This program runs through a calculation of interest rate by month

def compound(charge, min_payment, apr):
    '''
    Charge is a float that represents the amount charged to credit card
    min_payment is a float representing a percentage (0.1 = 10%)
    apr is a float also representing a percentage (0.1 = 10%)
    Calculates the new balance for each month
    return the balance after one year of minimum payments.
    '''
    def calc_interest(amount, apr):
        '''
        Takes amount, apr as floats and returns the amount of interest
            accrued       
        '''
        return 	apr / 12 * amount
 
    new_balance = charge  
    total_paid = 0

    for i in range(12):
        payment = new_balance * min_payment
        total_paid += payment
        unpaid_balance = new_balance - payment
        interest = calc_interest(unpaid_balance, apr)
#        print(i, new_balance, payment, unpaid_balance, interest) 
        new_balance = unpaid_balance + interest

    return round(new_balance, 2)


