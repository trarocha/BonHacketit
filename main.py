# Bon Hacketit 2020
# Tracy Rocha

import pandas as pd

# Choose restaurant
res = input("\nWelcome!\n\nSelect one of the following restaurants:\n\tPanda Express\n\tTaco Bell\n")
resValid = False
# print(res)

# Open the restuarant file, if available
while (resValid == False):
    if (res == "Panda Express"):
        names = ['Food', 'Type', 'Serving Size', 'Calories', 'Calories From Fat', 'Total Fat', 'Saturated Fat', 
            'Trans Fat', 'Cholesterol', 'Sodium', 'Total Carb', 'Dietary Fiber', 'Sugars', 'Protein']
        nameStart = 2
        nameEnd = 14
        df = pd.read_csv("PandaExpress.csv", sep=',', header=0)
        # print(df.head())
        resValid = True
    elif (res == "Taco Bell"):
        names = ['Food', 'Type', 'Calories', 'Calories From Fat', 'Total Fat', 'Saturated Fat', 'Trans Fat', 
            'Cholesterol', 'Sodium', 'Total Carbohydrates', 'Dietary Fiber', 'Sugars', 'Protein']
        nameStart = 2
        nameEnd = 13
        df = pd.read_csv("TacoBell.csv", sep=',', header=0)
        resValid = True
    else:
        res = input("Error: Please select a valid restaurant: ")

# Select type
print("\nSelect one of the following food types, type 'Food' to exclude beverages, or type 'All' to select full menu:")
types = df.Type.unique()
for i, str in enumerate(types):
    print("\t{0}".format(str))
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
cal = input("\nWould you like to set a calorie limit?\n\tYes\n\tNo\n")
calValid = False
while (calValid == False):
    if (cal == "Yes"):
        calMax = input("\nEnter a value between {0} and {1}: ".format(df.Calories.min(), df.Calories.max()))
        if calMax.isdigit():
            df = df[df.Calories <= int(calMax)]
            calValid = True
        else:
            calMax = input("Error: Enter a value between {0} and {1}: ".format(df.Calories.min(), df.Calories.max()))
    elif (cal == "No"):
        calValid = True
    else:
        cal = input("Error: Please select Yes or No: ")

# Select the first criteria
print("\nSelect your first criterion: ")
nameSubset = names[nameStart:nameEnd]
for i, str in enumerate(nameSubset):
    print("\t{0}".format(str))
crit1 = input()
# print(crit1)
crit1Valid = False
while (crit1Valid == False):
    if (crit1 in names[2:14]):
        # print("True\n")
        crit1Valid = True
    else:
        crit1 = input("Error: Please select a valid criterion: ")
sort1 = input("\nWould you like high or low {0}?\n\tHigh\n\tLow\n".format(crit1))
sort1Valid = False
while (sort1Valid == False):
    if (sort1 == "High" or sort1 == "Low"):
        # print("True\n")
        sort1Valid = True
    else:
        sort1 = input("Error: Please select 'High' or 'Low': ")

# Filter results
crit1 = crit1.replace(" ", "")
df_sub1 = df[crit1]
q_df = df_sub1.quantile([.25, .75])
if (sort1 == "High"):
    df = df.query("{0} >= {1}".format(crit1, q_df[0.75]))
    df = df.sort_values(by=crit1, ascending=False)
    print(df)
elif (sort1 == "Low"):
    df = df.query("{0} <= {1}".format(crit1, q_df[0.25]))
    df = df.sort_values(by=crit1, ascending=True)
    print(df)

# Select the second criteria
print("\nSelect your second criterion: ")
for i, str in enumerate(nameSubset):
    print("\t{0}".format(str))
crit2 = input()
# print(crit1)
crit2Valid = False
while (crit2Valid == False):
    if (crit2 in names[2:14]):
        # print("True\n")
        crit2Valid = True
    else:
        crit2 = input("Error: Please select a valid criteria: ")
sort2 = input("\nWould you like high or low {0}?\n\tHigh\n\tLow\n".format(crit2))
sort2Valid = False
while (sort2Valid == False):
    if (sort2 == "High" or sort2 == "Low"):
        # print("True\n")
        sort2Valid = True
    else:
        sort2 = input("Error: Please select 'High' or 'Low': ")

# Filter results
crit2 = crit2.replace(" ", "")
df_sub2 = df[crit2]
q_df = df_sub2.quantile([.25, .75])
if (sort2 == "High"):
    df = df.query("{0} >= {1}".format(crit2, q_df[0.75]))
    df = df.sort_values(by=crit2, ascending=False)
    print(df)
elif (sort2 == "Low"):
    df = df.query("{0} <= {1}".format(crit2, q_df[0.25]))
    df = df.sort_values(by=crit2, ascending=True)
    print(df)

print("\n")