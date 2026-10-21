#LoanPayment.py

"""
This program will take the principle payment, yearly interest rate, and length of the loan in years.
This program will then display the monthly payment, the total payments, and the total interest.
This program will then display a loan amortization table.
"""

import math


#This function takes in the loan_amount(principle), the annual interest rate(interest), and the length in years(years) and will return the monthly payment
def loan_payment(principle, interest, years):
    payment = (principle * interest / 12) / (1 - math.pow(1 + interest / 12, -12 * years))
    return payment


#These statments gather the loan amount, annual interest rate, and length in years of the loan from the user
loan_amount = int(input("Enter the loan amount: "))
annual_interest = float(input("Enter annual rate as a decimal: "))
number_of_years = int(input("Enter the number of years of the loan: "))


#These statements calculate the monthly payment(by calling the loan_payment function), the total that will be paid towards the loan, and how much of that total payment will be interest.
monthly_payment = loan_payment(loan_amount, annual_interest, number_of_years)
total_payments = 12 * monthly_payment * number_of_years
total_interest = total_payments - loan_amount


#These print statements display monthly payment, total payment, and total interest paid to the user
print(f"\nThe monthly payment will be ${monthly_payment:.2f}")
print(f"The total payments over {number_of_years} years will be ${total_payments:.2f}")
print(f"The total interest paid over {number_of_years} years will be ${total_interest:.2f}\n\n")


#These statments create the loan amortization table to show your remaining balance and how much of your payments go to interest and the loan amount each month.
print("Loan Amortization Table:\n")
print("Month\tInterest Payment\tPrinciple Payment\tRemaining Balance")
remaining_balance = loan_amount
for month in range(1,12 * number_of_years + 1):
    interest_payment = annual_interest * remaining_balance / 12
    principle_payment = monthly_payment - interest_payment
    remaining_balance -= principle_payment
    print(f"{month}\t\t{interest_payment:.2f}\t\t\t\t{principle_payment:.2f}\t\t\t\t{remaining_balance:.2f}")
