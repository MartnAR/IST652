name = input("What is your name?\n")
print('Welcome to the class, {:s}.'.format(name))
inp = input('Please enter a Celsius temperature:\n')
cel = float(inp) 
fahren = (9.0/5.0 * cel) + 32.0
floatFahren = float(fahren) 
print('The temperature you entered in Celsius, {:.2f}, is {:.2f} in degrees Fahrenheit.'.format(cel, floatFahren))
