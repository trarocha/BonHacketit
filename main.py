# Bon Hacketit 2020
# Tracy Rocha

import pandas as pd

# Choose restaurant
res = input("Welcome!\nSelect one of the following restaurants:\n\tPanda Express\n")
resValid = False
# print(res)

# Open the restuarant file, if available
while (resValid == False):
    if (res == "Panda Express"):
        names = ['Food', 'Type', 'ServingSize', 'Calories', 'CaloriesFromFat', 'TotalFat', 'SaturatedFat', 
            'TransFat', 'Cholesterol', 'Sodium', 'TotalCarb', 'DietaryFiber', 'Sugars', 'Protein']
        df = pd.read_csv("PandaExpress.csv", sep=',', header=0, names=names)
        # print(df.head())
        resValid = True
    else:
        res = input("Error: Please select a valid restaurant: ")

# Select type
print("Select one of the following food types, or type 'All' to select full menu:")
print("\t", end='')
print(df.Type.unique())
typ = input()
typValid = False
while (typValid == False):
    if (typ in df.Type.unique()):
        df = df[df.Type == typ]
        # print(df.head())
        typValid = True
    elif (typ == "All"):
        typValid = True
        # print(df.head())
    else:
        typ = input("Error: Please select a valid type: ")
        

# Select the first criteria
print("Please select your criteria to filter by: ")
i = 2
while i <= 11:
    print("\t")
    print(names[i], end='\t')
    print(names[i + 1], end='\t')
    print(names[i + 2])
    i += 3
crit1 = input()
# print(crit1)
crit1Valid = False
while (crit1Valid == False):
    if (crit1 in names[2:14]):
        # print("True\n")
        crit1Valid = True
    else:
        crit1 = input("Error: Please select a valid criteria: ")
sort1 = input("Would you like high or low {0}? Type 'High' or 'Low' to select: ".format(crit1))
sort1Valid = False
while (sort1Valid == False):
    if (sort1 == "High" or sort1 == "Low"):
        # print("True\n")
        sort1Valid = True
    else:
        sort1 = input("Error: Please select 'High' or 'Low': ")

# Filter results
q_df = df.ServingSize.quantile([.25, .75])
if (sort1 == "High"):
    df = df[df[sort1] >= q_df[0.75]]
    print(df.head())
elif (sort1 == "Low"):
    df = df[df.ServingSize <= q_df[0.75]]
    print(df.head())