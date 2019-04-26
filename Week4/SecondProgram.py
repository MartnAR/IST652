# Calculate numbers
# Created by: Martin Alonso
# Date created: 2019-04-16
# Purpose: prompt user for numbers until user says 'done!'. Calculates total numbers, number of numbers inputted, and average numbers entered. 

import numpy as np 

numbers = []

# Take input from user
while True:
	number = input("Please insert a number:")
	
	try:
		number_flt = float(number)
		numbers.append(number_flt)
	except:
		if number == "done!":
			len_number = len(numbers)
			sum_number = np.sum(numbers)
			avg_number = np.mean(numbers)
			print("You inserted {} numbers. The sum of these is {} and their average is {}.".format(len_number, sum_number, avg_number))
			break
		else:
			print("Please insert a number or 'done!' if you're finished.")

