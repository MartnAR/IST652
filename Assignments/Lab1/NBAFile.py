# IST652: Lab 1 
# NBAfile.py
# Created by: Martin Alonso
# Date created: 2019-04-10

# Purpose: Takes as input a file with data regarding an NBA team, it's attendance, and the average ticket price. Returns 
# a string summarising the data in the file. 

# Asks for the file input
file = input("Please input a file in your directory: \n")

# Reads the file. If the file does not exist in the directory, prints error message and closes. 
try: 
    NBAfile = open(file, "r")
except:
    print("File is not in directory. Please move the file to the correct directory.")

# Initiates an empty list to store the cleaned file data
NBAlist = []

# Iterate over every line in the text file, returning a list of lists
for line in NBAfile: 
    line_clean = line.strip()
    text_line = line_clean.split()
    NBAlist.append(text_line)

# Iterates over the list, printing each teams attendance and average ticket price
for team in NBAlist:
    print("The attendance at {} was {} and the ticket price was ${}".format(team[0], team[1], team[2]))
