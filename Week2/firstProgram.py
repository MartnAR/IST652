# Calculate pay
# Created by: Martin Alonso
# Date created: 2019-04-06
# Purpose: calculate pay from hours worked and rate of pay 

# Take inputs from the user 
hours = input("How many hours worked? ")
pay_rate = input("What is the pay rate? ")

# Convert hours and pay_rate to float; calculate pay
pay = float(hours) * float(pay_rate)

# Return pay 
print("Your payment is ${:.2f}".format(pay))
