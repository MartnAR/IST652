# List and loops activity
# Exercise 1
# Print only the characters with a length greater than 2. 

# Create a list of ten items 
samples = ['oh', 'trout', 'yelich', 'harper', 'ryu', 'choi', 'ohtani', 'at', 'sb', 'warp']

# Print strings that have a length greater than 2
for i in samples: 
    if len(i) > 2:
        print(i)

print('\n')

# Exercise 2
# Print only the characters that have a length between 2 and 5. 

for i in samples:
    if len(i) > 2 and len(i) < 5:
        print(i)