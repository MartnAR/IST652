# NBA file read
# Created by: Martin Alonso
# Date created: 2019-04-06
# Purpose: read NBA attendance and ticket price text file, store in list, clean white space, and display results

# Import pandas package to load text file
import re
import os 

os.chdir("C:/Users/malon/Documents/Syracuse University/IST 652 Scripting for Data Analysis/IST652-Scripting-for-Data-Analysis/Week2")

# Load text file
NBAfile = open("NBA-Attendance-1989.txt", "r")

# Initiate count object empty list to store text data
count = 0
NBAlist = []

# Iterate over every line in the text file, returning a list of lists
for line in NBAfile: 
    count += 1
    line_clean = line.strip()
    text_line = line_clean.split()
    NBAlist.append(text_line)

# Print the number of lines read and the team for each line
print("Number of teams: {:d}".format(count))
for team in NBAlist: 
    print("Team: ", team)