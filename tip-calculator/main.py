
print("Welcome to Tip calculator")
meal_cost = float(input("please enter the total bill "))
tip = int(input("What percentage tip would you like to give? 10, 12, 15? "))
people_n = int(input("How many people to split the bill? "))

bill_plus_tip = meal_cost * tip / 100 + meal_cost
split_bill = bill_plus_tip / people_n
print(f"Each person should pay: %.2f" % split_bill)
