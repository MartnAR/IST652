# IST652 Homework 1
# Created by: Martin Alonso
# Date created: 2019-04-24

# Purpose:
# 1. Program must read data
# 2. Data must be converted to correct type and cleaned. 
# 3. Data must be processed and answer two questions (graphs are optional). 

# Data source: https://www.kaggle.com/martinellis/nhl-game-data/version/3#
# Secondary source: https://www.hockey-reference.com/

# Packages to be used 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re 

# File to be imported 
file = input("Which file do you wish to import?: \n")

# Load the file
try: 
    df = pd.read_csv(file)
    print(df.head())

    # Extract column names. If columns names end in '_id', change column type to object.
    # Loop stores column names with '_id' or 'Id' and asks the user if they want to upload a file that contains the id files for these columns
    col_names = df.columns.values
    id_list = []
    for i in range(len(col_names)): 
        if re.search('_*[Ii]d', col_names[i]):
            df.iloc[:, i] = df.iloc[:, i].astype(object)
            col = col_names[i]
            id_list.append(col)

    # Prints number of columns changed to object type and list of column names. 
    print("The following {} columns are id columns: ".format(len(id_list)), id_list)

    # Counts number of files added. 
    new_file_count = 0
    
    # Ask user if they want to upload id files
    if len(id_list) > 0:
        while True:
            answer = input("Do you want to add an identification file to merge? ")
            if answer == "Yes" or answer == "yes": 
                new_file_count += 1
                # Imports new file to merge with the first file imported 
                new_file = input("Please add file: ")
                try:
                    nf = pd.read_csv(new_file)
                    # Searches new columns to match Id columns
                    nf_columns = nf.columns.values
                    nf_id_list = []
                    for i in range(len(nf_colnames)): 
                        if re.search('_*[Ii]d', nf_colnames[i]):
                            nf.iloc[:, i] = nf.iloc[:, i].astype(object)
                            col = nf_colnames[i]
                            nf_id_list.append(col)
                   
                    # Extracts list of columns to merge the dataframes by 
                    try:
                        df_merger = list(set(id_list).intersection(nf_id_list))
                        df = df.merge(nf, how='left', on=df_merger)
                    except:
                        print("Files can not be merged.")
                except: 
                    print("File not in directory.")
            elif answer == "No" or answer == "no": 
                # Breaks loop
                print("{} files added.".format(new_file_count))
                break
            else:
                # Anything other than 'yes' or 'no' prompts the user to type one of these inputs. 
                print("Invalid command. Input 'Yes' to add files, 'No' to exit file addition.")
    
    # Prints first five observations of new data frame
    print(df.head())

except: 
    print("File not in directory. Please move file to directory.")
