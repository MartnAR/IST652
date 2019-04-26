# Exercise 1
## What will the following programs print
def fred():
    print("Zap")

def jane():
    print("ABC")

jane()
fred()
jane()

# Exercise 2
## Rewrite the pay computation program that you created in Week 2. 
def computepay(hours, rate):
    pay = hours * rate * 1.0556
    pay = round(pay, 2)
    return(pay)
