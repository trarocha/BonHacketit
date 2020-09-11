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
        names = ['Food', 'Type', 'Serving Size (oz)', 'Calories', 'Calories From Fat (g)', 'Total Fat (g)', 'Saturated Fat (g)', 
            'Trans Fat (g)', 'Cholesterol (mg)', 'Sodium(mg)', 'Total Carb (g)', 'Dietary Fiber (g)', 'Sugars (g)', 'Protein (g)']
        df = pd.read_csv("PandaExpress.csv", header=0, names=names)
        # print(df.head())
        resValid = True
    else:
        res = input("Error: Please select a valid restaurant: ")

# Select type
print("Select one of the following food types, or type 'all' to select full menu:\n")
print(df.Type.unique)
typ = input()
typValid = False

# Select the first criteria
print("Please select your first criteria: ")
i = 2
while i <= 11:
    print("\t")
    print(names[i], end='\t')
    print(names[i + 1], end='\t')
    print(names[i + 2])
    i += 3
crit1 = input()
# print(crit1)
