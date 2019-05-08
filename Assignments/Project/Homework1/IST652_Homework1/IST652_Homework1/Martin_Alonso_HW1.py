# IST652 Homework 1
# Created by: Martin Alonso
# Date created: 2019-04-24

# Purpose:
# Prompts the user to input a comma-separated value file; identifies columns that should be id columns, and prompts the user to pick one of these 
# columns to group the data by. Outputs a summarized csv file grouping by the selected id column plus two graphs showing goals per selected 
# grouped column and shots per goals of selected grouped column, as a bar plot and scatter plot. 

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

    # Extract column names. If columns names end in '_id', change column type to object.
    # Loop stores column names with '_id' or 'Id' and asks the user if they want to upload a file that contains the id files for these columns
    col_names = df.columns.values
    id_list = []
    for i in range(len(col_names)): 
        if re.search('_*[Ii]d', col_names[i]):
            df.iloc[:, i] = df.iloc[:, i].astype(object)
            col = col_names[i]
            id_list.append(col)

    # Prints first five observations of new data frame
    print(df.head())
    
    # Prints number of columns changed to object type and list of column names. 
    print("The following {} columns are id columns: ".format(len(id_list)), id_list)
    grouper = input("By which id column would you like to summarise your data? \n")

    try: 
        match = [s for s in id_list if grouper in s]

        # Group data by selected column.
        group_file = df.groupby(match)[['goals', 'shots', 'timeOnIce']].sum().reset_index()
        group_file['timeOnIce'] = group_file['timeOnIce']/60.0
        group_file['goals_per_60'] = group_file['goals'] * 60 / group_file['timeOnIce']
        group_file['shots_per_60'] = group_file['shots'] * 60 / group_file['timeOnIce']
        
        # File name to export
        file_name = grouper + 'stats per 60.csv'
        group_file.to_csv(file_name, index=False)
        print('Exporting shots and goals per 60 minutes')
        print(group_file.head())
            
        # Plot average goals per 60 minutes per team
        sns.catplot(x=grouper, y='goals_per_60', data=group_file, kind='bar')
        _ = plt.xticks(rotation=90)
        _ = plt.xlabel('Teams')
        _ = plt.ylabel('Goals per 60 minutes')
        _ = plt.title('Goals per 60 minutes of player time on ice')
        plt.show()

        def label_point(x, y, val, ax):
            """
            Creates a label to attach to each point on a scatter plot
            """
            a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
            for i, point in a.iterrows():
                ax.text(point['x']+.02, point['y'], str(point['val']))

        # Plot average goals per 60 minutes by average shots per 60 minutes 
        sns.scatterplot(x='shots_per_60', y='goals_per_60', data=group_file, hue=grouper, legend=False)
        _ = plt.xticks(rotation=90)
        _ = plt.xlabel('Shots per 60 minutes')
        _ = plt.ylabel('Goals per 60 minutes')
        _ = plt.title('Goals per shots by 60 minutes of player time on ice')
        label_point(group_file.shots_per_60, group_file.goals_per_60, group_file[grouper], plt.gca())
        plt.show()         

    except: 
        print("Can't group by selected column.")    

except: 
    print("File not in directory. Please move file to directory.")

