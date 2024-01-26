# Pseudocode
# 1. Create a program that will calculate income taxes
# 2. Follow the rules:
# First $10,000 = 0 rate in %
# Next $10,000 = 10 rate in %
# Proceeding = 20 rate in %

user_income = input("Please input your income: ")
if user_income.isdigit():
    user_income = int(user_income)
else:
    print("Invalid, please input numbers.")

if user_income <= 10000:
    tax_rate = 0
elif user_income <= 20000:
    first_ten_thou = user_income - 10000

    tax_rate = first_ten_thou * 10 / 100