# Create a dictionary; store five contacts with their phone numberso, sort list in alphabetical order, and print the dictionary. 
my_phonebook = {"Dani": "511-343-9053", 
                "Harry": "673-404-3392", 
                "Mum": "903-323-9987", 
                "Alonso": "934-221-4343", 
                "Santiago": "903-322-1943"}

# Sort elements in phonebook and print them out. 
for elem in sorted(my_phonebook.items()):
    print(elem[0], ': ', elem[1])
