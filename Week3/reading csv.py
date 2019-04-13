import os 
import pandas as pd 

os.getcwd()
os.chdir("C:/Users/malon/Documents/Syracuse University/IST 652 Scripting for Data Analysis/IST652/Week3")
infile = "states_data.tsv"

states_df = pd.read_csv(infile, delimiter="\t")
states_df = states_df.dropna()
states_df["Area (Sq Mi)"] = states_df["Area (Sq Mi)"].astype(str).apply(lambda x: x.replace(",", "")).astype(int)
states_df["Population*"] = states_df["Population*"].astype(str).apply(lambda x: x.replace(",", "")).astype(int)

states_list = []

for i in range(len(states_df)):
    state = {}
    state["name"] = states_df.iloc[i, 0]
    state["abbrev"] = states_df.iloc[i, 1]
    state["code"] = states_df.iloc[i, 2]
    state["area"] = states_df.iloc[i, 3]
    state["pop"] = states_df.iloc[i, 4]
    states_list.append(state)

for state in states_list:
    print("State: ", state["name"], "Abbrev: ", state["abbrev"], "Pop: ", state["pop"])