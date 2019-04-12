# Initiate string 
my_string = "X-DSPAM-Confidence:0.8475"

# Find the colon and convert the string to float
colon = my_string.find(":")
confidence = float(my_string[colon+1:])

# Print the confidence result
"The confidence is: {:.2f}".format(confidence)