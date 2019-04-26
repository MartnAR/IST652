# Load the packages
import pandas as pd 

# Create a dictionary 
persondict = {'person':['Bob','Alice','Steve'], 'age':[32, 24, 64], 'weight':[128, 86, 95]}
persontable = pd.DataFrame(persondict, columns=['person', 'age', 'weight'])

# 1. Index the table by person
persontable = persontable.set_index('person')
persontable

# 2. Stack the index into a tall object
result = persontable.stack()
result

# 3. Reset the index
stack_table = result.reset_index()

# 4. Rename the columns to 'person', 'attribute', 'value'
stack_table.columns = ['person', 'attribute', 'value']
stack_table

# 5. Convert back to original unstacked data
original = result.unstack()
original

# 6. Pivot the table 
personpivot = stack_table.pivot('person', 'attribute', 'value')
personpivot