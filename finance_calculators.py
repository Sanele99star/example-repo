import math
print ("Investment - to calculate the amount of interest you'll earn on your investment.\nBond - to calculate the amount you'll have to pay on a home loan.\n ")
financial_calculator = input ("Enter either 'Investment' or 'Bond' from the menu above to proceed: ")
# The user will direct the direction of the code by choosing either 'Investment' or 'Bond' from the menu above.
if financial_calculator in ["Bond","BOND","bond"]:
    present_value = float(input("Enter the present value of the house: "))
    bond_interest_rate = float(input("Enter the interest rate: "))/100/12
    months_to_pay = float(input("Enter the number of months you plan on taking to repay the bond: "))
    repayment = bond_interest_rate*present_value/1 - ((1+bond_interest_rate)**(-months_to_pay))
    print (f"The amount you'll have to pay on a home loan is: R{repayment}")
elif financial_calculator in ["Investment","Investment","INVESTMENT"]:
    principal_amount = float(input("Enter the amount of money that you are depositing: "))
    interest_rate = float(input("Enter the interest rate: "))/100
    years = float(input("Enter the number of years you plan on investing for: "))
    interest = input("Do you want simple or compound interest? ")
    if interest == "simple" or "Simple":
        A = principal_amount*(1 + interest_rate*years)
        print (f"The amount of interest you'll earn on your investment is: R{A}")
    elif interest == "compound" or "Compound":
        A = principal_amount*math.pow((1+interest_rate),years)
        print (f"The amount of interest you'll earn on your investment is: R{A}")
else:
    print ("Invalid input. Please try again.")


