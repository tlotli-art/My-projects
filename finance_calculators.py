# Investment and Bond calculator

import math


# Display a message informing user to choose options
print("Choose either 'investment' or 'bond' from the menu below to proceed: ")


investment_bond = input('''investment               - to calculate the amount of interest you'll earn on interest
bond                     - to calculate the amount you'll have to pay on a home loan
>> ''')                   


# Alter the user response to lower caps 
calculator = investment_bond.lower()


# If user chooses investment,they must choose between simple and compound and they must input variables for the calculation
if calculator == "investment":

    money_deposit = float(input("Please input the amount of money you wish to deposit: R"))

    interest_rateinv = float(input("Please enter the interest rate, 'NB' please do not includ the '%' next to your number: "))

    time = int(input("Please enter the number of years you plan on investing for: "))

    interest = input("What interest do you want?(simple/ compound): ")

    interest_calc = interest.lower()


# Formula's to calculate for simple or compuund interest, if user doesnt pick any of the two print error message
    if interest_calc == "simple":

        total_amount = money_deposit *(1 + (interest_rateinv/100) * time)

    elif interest_calc == "compound":

        total_amount = money_deposit * math.pow((1 + (interest_rateinv/100)), time)

    else:
        print("ERROR! You have entered an incorrect word, please check the spelling and try again")


# Print the total amount
    if calculator == "investment":

        print("Your total amount is: R" + str(round(total_amount,2)))


# if user chooses bond, they must input variables needed for the calculation 

elif calculator == "bond":

    value = float(input("What is the present value of the house? : R"))

    interest_ratebon = float(input("Please enter the interest rate, 'NB' please do not includ the '%' next to your number: "))

    months = int(input("How many months do you plan to repay the bond? : "))


# formula to calculate to calculate bond repayment
    if calculator == "bond":

        rate = interest_ratebon/ 100

        total_repayment = ((rate/12) * value)/(1 - math.pow((1  + (rate/12)), - months))


# Display the total amount
    if calculator == "bond":

        print("The total monthly repayment is: R" + str(round(total_repayment,2)))


# If user types wrong option type error message    
else:
    print("ERROR! You have entered an incorect word, please check the spelling and try again")
