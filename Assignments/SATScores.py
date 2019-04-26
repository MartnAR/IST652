# IST652: Quiz 1 
# SATScores.py
# Created by: Martin Alonso
# Date created: 2019-04-22

# Purpose: Takes a file with SAT scores by state, reads the file, and prints the state with the highest SAT score and the states with Math Scores above 500. 

# Asks for the file input
file = input("Please input a file in your directory: \n")

# Reads the file. If the file does not exist in the directory, prints error message and closes. 
try: 
    SATscores = open(file, "r")
except:
    print("File is not in directory. Please move the file to the correct directory.")

# Initiates an empty list to store the cleaned file data
SATlist = []

# Iterate over every line in the text file, returning a list of lists
for line in SATscores: 
    line_clean = line.strip()
    text_line = line_clean.split()
    SATlist.append(text_line)

# Initiates an empty list to store the highest Verbal score
max_verbal_score = ["state", 0]

for i in range(len(SATlist)):
    state = SATlist[i][0]
    verbal_score = int(SATlist[i][1])
    if max_verbal_score[1] > verbal_score:
        max_verbal_score[0], max_verbal_score[1] = max_verbal_score[0], max_verbal_score[1]
    else:
        max_verbal_score[0], max_verbal_score[1] = state, verbal_score

print("The state with the highest verbal score is {} with {}".format(max_verbal_score[0], max_verbal_score[1]))

# Print out the states with a math score above 500
for i in range(len(SATlist)):
    state = SATlist[i][0]
    math_score = int(SATlist[i][2])
    if math_score >= 500:
        print("{}'s math score was {}".format(state, math_score))
