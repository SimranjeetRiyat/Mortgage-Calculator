import math

mortgage_amount = 375000

initial_mortgage_years = 25
remaining_mortgage_years = 25
accumulated_mortgage_years = 0

initial_fixed_term = 3
next_fixed_term = 5

initial_interest_rate = 0.046
next_fixed_term_interest_rate = 0.035
interest_rate = initial_interest_rate
   
def monthly_payment(mortgage_amount,mortgage_years,interest_rate):
    r = interest_rate / 12
    base = 1 + r
    n = mortgage_years*12
    monthly_payment = mortgage_amount*(r*math.pow(base,n) / (math.pow(base,n) - 1))
    return monthly_payment


def remaining_amount_after_term(mortgage_amount, mortgage_years, interest_rate, fixed_term,potential_overpayment):
    r = interest_rate / 12
    base = 1 + r
    n = mortgage_years * 12
    fixed_term = fixed_term * 12
    
    monthly_payment_amount = monthly_payment(mortgage_amount, mortgage_years, interest_rate)
    
    if potential_overpayment > 0:
        monthly_payment_amount = potential_overpayment
    
    remaining_amount = mortgage_amount * math.pow(base, fixed_term) - monthly_payment_amount * (math.pow(base, fixed_term) - 1) / r
    
    return remaining_amount


for i in range(6):
    if i ==0:
        accumulated_mortgage_years = initial_fixed_term
        print(f"Monthly payment First 3 Year Term at {interest_rate*100}%: {monthly_payment(mortgage_amount,initial_mortgage_years,interest_rate):.2f}")

        potential_overpayment = float(input("Potential Overpayment: "))
        mortgage_amount = remaining_amount_after_term(mortgage_amount,initial_mortgage_years,interest_rate,initial_fixed_term,potential_overpayment)

        print(f"Remaining Amount After {initial_fixed_term} years: {mortgage_amount:.2f}")
    elif i == 1:
        remaining_mortgage_years = initial_mortgage_years - initial_fixed_term
        accumulated_mortgage_years = accumulated_mortgage_years + next_fixed_term
        print(f"Monthly payment During This 5 Year Term at {next_fixed_term_interest_rate*100}%: {monthly_payment(mortgage_amount,remaining_mortgage_years,next_fixed_term_interest_rate):.2f}")
        
        potential_overpayment = float(input("Potential Overpayment: "))
        
        mortgage_amount = remaining_amount_after_term(mortgage_amount,remaining_mortgage_years,next_fixed_term_interest_rate,next_fixed_term,potential_overpayment)
        print(f"Remaining Amount After {accumulated_mortgage_years} years: {mortgage_amount:.2f}")

    else:
        next_fixed_term_length = float(input("Next Fixed Term Length: "))
        next_fixed_term_interest_rate = float(input("Next Fixed Term Interest Rate %: "))/100
        remaining_mortgage_years = remaining_mortgage_years - next_fixed_term
        
        accumulated_mortgage_years = accumulated_mortgage_years + next_fixed_term_length
        print(f"Monthly payment For This {int(next_fixed_term_length)} Year Term at {next_fixed_term_interest_rate*100}: {monthly_payment(mortgage_amount,remaining_mortgage_years,next_fixed_term_interest_rate):.2f}")
        
        potential_overpayment = float(input("Potential Overpayment: "))
        mortgage_amount = remaining_amount_after_term(mortgage_amount,remaining_mortgage_years,next_fixed_term_interest_rate,next_fixed_term,potential_overpayment)
        
        print(f"Remaining Amount After {accumulated_mortgage_years} years: {mortgage_amount:.2f}")

