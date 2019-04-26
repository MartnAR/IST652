# IST652: Lab 2
# Fruit.py
# Created by: Martin Alonso
# Date created: 2019-04-22

# Consider the following two dictionaries
stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}

# a. Show the expression that gets the value of the stock dictionary at the key "orange". 
print(stock["orange"])

# Show a statement that adds an item to the stock dictionary called "cherry" with an integer value and 
# adds "cherry" to the prices dictionary with a numeric value.
stock["cherry"] = 5
prices["cherry"] = 0.2

# b. Write the code for a loop that iterates over the stock dictionary and prints each key and value.
for k, v in stock.items():
    print(k, v)

# c. Suppose that we have a list: 
groceries = ["apple", "banana", "pear"]

# Write the code that will sum the total number in stock of the items in the groceries list. 
grocery_dict = {k: v for k, v in stock.items() if k in groceries}
grocery_stock = sum({v for k, v in stock.items() if k in groceries})
print(grocery_dict)
print(grocery_stock)

# d. Write the code that can print out the total value in stock of all the items. This program can iterate over the stock dictionary and 
# for each item multiply the number in stock times the price of that item in the prices ditionary. 
stock_price = []
for k, v in stock.items():
    product_value = stock[k] * prices[k]
    stock_price.append(product_value)
    print("The total value of {} {}s is {}".format(stock[k], k, product_value))


print("The total value in stock is {}".format(sum(stock_price)))

