# Bon Hacketit 2020
# Tracy Rocha

import pandas as pd

# Choose restaurant
res = input("\nWelcome!\n\nSelect one of the following restaurants:\n\tPanda Express\n\tTaco Bell\n\n")
resValid = False
# print(res)

# Open the restuarant file, if available
while (resValid == False):
    if (res == "Panda Express"):
        names = ['Food', 'Type', 'ServingSize', 'Calories', 'CaloriesFromFat', 'TotalFat', 'SaturatedFat', 
            'TransFat', 'Cholesterol', 'Sodium', 'TotalCarb', 'DietaryFiber', 'Sugars', 'Protein']
        nameStart = 2
        nameEnd = 14
        df = pd.read_csv("PandaExpress.csv", sep=',', header=0, names=names)
        # print(df.head())
        resValid = True
    elif (res == "Taco Bell"):
        names = ['Food', 'Type', 'Calories', 'CaloriesFromFat', 'TotalFat', 'SaturatedFat', 'TransFat', 
            'Cholesterol', 'Sodium', 'TotalCarbohydrates', 'DietaryFiber', 'Sugars', 'Protein']
        nameStart = 2
        nameEnd = 13
        df = pd.read_csv("TacoBell.csv", sep=',', header=0, names=names)
        resValid = True
    else:
        res = input("Error: Please select a valid restaurant: ")

# Select type
print("Select one of the following food types, type 'Food' to exclude beverages, or type 'All' to select full menu:")
print("\t", end='')
print(df.Type.unique())
typ = input()
typValid = False
while (typValid == False):
    if (typ in df.Type.unique()):
        df = df[df.Type == typ]
        # print(df.head())
        typValid = True
    elif (typ == "Food"):
        df = df[df.Type != 'Beverage']
        typValid = True
    elif (typ == "All"):
        typValid = True
        # print(df.head())
    else:
        typ = input("Error: Please select a valid type: ")
        
# Option to set calorie limit
cal = input("Would you like to set a calorie limit? Type 'Yes' or 'No': ")
calValid = False
while (calValid == False):
    if (cal == "Yes"):
        calMax = input("Enter a value between {0} and {1}: ".format(df.Calories.min(), df.Calories.max()))
        if calMax.isdigit():
            df = df[df.Calories <= int(calMax)]
            calValid = True
        else:
            calMax = input("Error: Enter a value between {0} and {1}: ".format(df.Calories.min(), df.Calories.max()))
    elif (cal == "No"):
        calValid = True
    else:
        cal = input("Error: Please select Yes or No")

# Select the first criteria
print("Please select your criteria to filter by: ")
print(names[nameStart:nameEnd])
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
df_sub1 = df[crit1]
q_df = df_sub1.quantile([.25, .75])
if (sort1 == "High"):
    df = df.query("{0} >= {1}".format(crit1, q_df[0.75]))
    print(df)
elif (sort1 == "Low"):
    df = df.query("{0} <= {1}".format(crit1, q_df[0.25]))
    print(df)

# Select the second criteria
print("Please select your criteria to filter by: ")
print(names[nameStart:nameEnd])
crit2 = input()
# print(crit1)
crit2Valid = False
while (crit2Valid == False):
    if (crit2 in names[2:14]):
        # print("True\n")
        crit2Valid = True
    else:
        crit2 = input("Error: Please select a valid criteria: ")
sort2 = input("Would you like high or low {0}? Type 'High' or 'Low' to select: ".format(crit2))
sort2Valid = False
while (sort2Valid == False):
    if (sort2 == "High" or sort2 == "Low"):
        # print("True\n")
        sort2Valid = True
    else:
        sort2 = input("Error: Please select 'High' or 'Low': ")

# Filter results
df_sub2 = df[crit2]
q_df = df_sub2.quantile([.25, .75])
if (sort2 == "High"):
    df = df.query("{0} >= {1}".format(crit2, q_df[0.75]))
    print(df)
elif (sort2 == "Low"):
    df = df.query("{0} <= {1}".format(crit2, q_df[0.25]))
    print(df)