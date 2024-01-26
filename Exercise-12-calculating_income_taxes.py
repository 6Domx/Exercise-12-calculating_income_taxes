# Pseudocode
# 1. Create a program that will calculate income taxes
# 2. Follow the rules:
# First $10,000 = 0 rate in %
# Next $10,000 = 10 rate in %
# Proceeding = 20 rate in %

# For asking user income
user_income = input("Please input your income: ")
if user_income.isdigit():
    user_income = int(user_income)
else:
    print("Invalid, please input numbers.")

if user_income <= 10000:
    tax_rate = 0

# 0 rate in first 10,000
elif user_income <= 20000:
    first_ten_thou = user_income - 10000

    tax_rate = first_ten_thou * 10 / 100

else: 
# first rate 
    tax_rate = 0
# second rate
    tax_rate = 10000 * 10 / 100
# third rate
    tax_rate += (user_income - 20000) * 20 / 100

# For printing tax payable
print("Your need to pay $", tax_rate)