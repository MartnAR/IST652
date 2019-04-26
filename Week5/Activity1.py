# Load packages
import numpy as np 
import pandas as pd 

# Load state dictionary data 
state_data = {'State':['Alabama','Alaska','Arizona','Arkansas'],'PostCode':['AL','AK','AZ','AR'],'Area':['52,423','656,424','*','53,182'],'Pop':['4,040,587','550,043','3,665,228','2,350,750']}

# 1. Create a pd.DataFrame from the state_data dictionary 
stdf = pd.DataFrame(state_data, columns=['State', 'PostCode', 'Area', 'Pop'])

# 2. Display the table 
stdf

# 3. Index the table using the 'State' columns
stdf = stdf.set_index('State')
stdf

# 4. Replace the '*' in the 'Area' column with '0'
stdf['Area'] = stdf['Area'].replace('*', '0')

# 5. Define a function that replaces ',' with ''
def item_replace(xstr):
    return(xstr.replace(',', ''))

# 6. Use the function to replace ',' in 'Area' and 'Pop'
stdf['Area'] = stdf['Area'].map(item_replace)
stdf['Pop'] = stdf['Pop'].map(item_replace)