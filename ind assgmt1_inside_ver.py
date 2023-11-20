import os
os.system('cls')

import sys

loan_calculations = []

#Option 1- Calculate a new loan
def monthly_instalment_calculator(loan_amount, annual_interest_rate,loan_terms):
    monthly_interest_rate = annual_interest_rate / 12
    no_of_payments = loan_terms * 12
    monthly_instalment = loan_amount * ((monthly_interest_rate*((1 + monthly_interest_rate)**no_of_payments))/(((1 + monthly_interest_rate)**no_of_payments) - 1))
    return monthly_instalment

def total_amount_payable_calculator(monthly_instalment, loan_terms):
    total_amount_payable = monthly_instalment * loan_terms * 12
    return total_amount_payable

def debt_service_ratio_calculator(monthly_income, monthly_financial_commitments):
    debt_service_ratio = (monthly_financial_commitments / monthly_income) * 100
    return debt_service_ratio

#Loan Details
def loan_details_display(loan_amount, annual_interest_rate, loan_terms, monthly_income, monthly_instalment, total_amount_payable, debt_service_ratio):
    print("\nLoan Details: ")
    print(f"Principal Loan Amount: RM{loan_amount}")
    print(f"Annual Interest Rate: {annual_interest_rate}%")
    print(f"Loan Terms: {loan_terms}years")
    print(f"Monthly Income: RM{monthly_income}")
    print("\nResults:")
    print(f"Monthly Instalment: RM{monthly_instalment: .2f}")
    print(f"Total Amount Payable: RM{total_amount_payable: .2f}")
    print(f"Debt Service Ratio(DSR): {debt_service_ratio: .2f}%")

def new_loan_calculator():
    print("\nCalculate New Loan:")

    #For user to input
    loan_amount = float(input("Enter your loan amount: "))
    annual_interest_rate = float(input("Enter the annual interest rate: "))
    loan_terms = int(input("Enter your loan terms: "))
    monthly_income = float(input("Enter your monthly income: "))
    monthly_financial_commitments = float(input("Enter your other monthly financial commitments: "))

    #To calculate
    monthly_instalment = monthly_instalment_calculator(loan_amount, annual_interest_rate,loan_terms)
    total_amount_payable = total_amount_payable_calculator(monthly_instalment, loan_terms)
    debt_service_ratio = debt_service_ratio_calculator(monthly_income, monthly_financial_commitments)

    #Check Eligibility
    eligibile = debt_service_ratio <= 70

     #To display loan details
    loan_details_display(loan_amount, annual_interest_rate, loan_terms, monthly_income, monthly_instalment, total_amount_payable, debt_service_ratio)
    
    if eligibile:
        print("\nYou are eligible for the Loan")
    else:
        print("\nYou are not eligible for the Loan") 

    #To store loan details
    loan_calculations.append({
        "Principal Loan Amount": loan_amount,
        "Annual Interest Rate": annual_interest_rate,
        "Loan Terms": loan_terms,
        "Monthly Income": monthly_income,
        "Other Monthly Financial Commitments": monthly_financial_commitments,
        "Monthly Instalment": monthly_instalment,
        "Total Amount Payable": total_amount_payable,
        "Debt Service Ratio": debt_service_ratio,
        "Eligibility": eligibile
    })

#Option 2 - Display all previous loan calculations
def previous_loan_calculations_display():    
    print("\nPrevious Loan Calculations: ")
    for index, loan in enumerate(loan_calculations, start=1):
        print(f"\nLoan Calculation {index}:")
        for key, value in loan.items():
            print(f"{key}: {value}")

#Main Menu
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Calculate New Loan")
        print("2. Display Previous Loan Calculations")
        print("3. Exit")

        option = input("Enter your option: ")

        if option == "1":
            new_loan_calculator()
        elif option == "2":
            previous_loan_calculations_display()
        elif option == "3":
            print("Exiting the program...")
            sys.exit()
        else:
            print("Invalid option. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()





        






