# Tracy Rocha
# Bon Hacketit 2020
# Narrow It Down
# Main program

import pandas as pd
from functions import openFile, getNames, quitProgram

# Welcome message
# User inputs restaurant
print("\nWelcome to Narrow It Down!\n\nThis program will filter a menu of your choice based off of two nutritional criteria that you select.")
print("Please note that all your answers are case-sensitive.")
print("\nIf you are using your own dataset, type the name (without the .csv extension).")
res = input("Otherwise, select one of the following restaurants:\n\tPanda Express\n\tTaco Bell\n\tMcDonalds\n")
resValid = False

# Open the restuarant file
# Get list with column names
while (resValid == False):
    df = openFile(res)
    try:
        if (df.shape != (0, 0)):
            names = list(df)        # Get names from dataframe
            names = getNames(names) # Format names
            nameStart = 2           # The first two columnns are assumed to be Food and Type
            nameEnd = len(names)    # Get total number of columns
            resValid = True         # Confirm that the restaurant is valid
    except AttributeError:
        res = input("Error: Please select a valid restaurant\n")

# Print a list of available food types
# If user selects one type: filter dataframe to include only that type
# If user selects "Food":   filter dataframe to include all types except "Beverage"
# If user selects "All":    do not change dataframe
print("\nSelect one of the following food types, type 'Food' to exclude beverages, or select 'All' to include full menu:")
types = df.Type.unique()
for i, str in enumerate(types):
    print("\t{0}".format(str))
typ = input()
typ = typ.strip()
typValid = False
while (typValid == False):
    if (typ in df.Type.unique()):
        df = df[df.Type == typ]
        typValid = True
    elif (typ == "Food"):
        df = df[df.Type != 'Beverage']
        typValid = True
    elif (typ == "All"):
        typValid = True
    else:
        typ = input("Error: Please select a valid type: ")
        
# Option to set a calorie limit
# If user selects "Yes": display limit of current subset of data
#                        filter dataframe to include all foods with calorie count less than or equal to specified value
# If user selects "No":  do not change dataframe
cal = input("\nWould you like to set a calorie limit?\n\tYes\n\tNo\n")
cal = cal.replace(" ", "")
calValid = False
while (calValid == False):
    if (cal == "Yes"):
        calMax = input("\nEnter a value between {0} and {1}: ".format(df.Calories.min(), df.Calories.max()))
        if calMax.isdigit():
            try:
                df = df[df.Calories <= int(calMax)]
                calValid = True
            except TypeError:
                quitProgram("Non-integer calorie value")
        else:
            calMax = input("Error: Enter a value between {0} and {1}: ".format(df.Calories.min(), df.Calories.max()))
    elif (cal == "No"):
        calValid = True
    else:
        cal = input("Error: Please select Yes or No: ")

# Select the first criterion
# Print list of all numerical criteria
# Check that user input matches a column name in the dataframe
print("\nSelect your first filter: ")
nameSubset = names[nameStart:nameEnd]
for i, str in enumerate(nameSubset):
    print("\t{0}".format(str))
crit1 = input()
crit1 = crit1.strip()
crit1Valid = False
while (crit1Valid == False):
    if (crit1 in names[nameStart:nameEnd]):
        crit1Valid = True
    else:
        crit1 = input("Error: Please select a valid filter: ")

# Choose whether to filter by high or low amount
sort1 = input("\nWould you like high or low {0}?\n\tHigh\n\tLow\n".format(crit1))
sort1 = sort1.replace(" ", "")
sort1Valid = False
while (sort1Valid == False):
    if (sort1 == "High" or sort1 == "Low"):
        sort1Valid = True
    else:
        sort1 = input("Error: Please select 'High' or 'Low': ")

# Remove space from user input in order to access dataframe
# Extract only the data relevant to the criterion.
# Find the upper and lower quantile of that data.
# If user selected "High":  filter dataframe to include only entries with values of the criterion greater than or equal to the 0.75 quantile
# If user selected "Low":   filter dataframe to include only entries with values of the crtierion less than or equal to the 0.25 quantile
# Print the resulting dataframe
crit1 = crit1.replace(" ", "")
df_sub1 = df[crit1]
try: 
    q_df = df_sub1.quantile([.25, .75])
except TypeError:
    quitProgram("Non-integer value in {0}".format(crit1))
if (sort1 == "High"):
    df = df.query("{0} >= {1}".format(crit1, q_df[0.75]))
    df = df.sort_values(by=crit1, ascending=False)
    print(df)
elif (sort1 == "Low"):
    df = df.query("{0} <= {1}".format(crit1, q_df[0.25]))
    df = df.sort_values(by=crit1, ascending=True)
    print(df)

# Select the second criterion
# Print list of all numerical criteria
# Check that user input matches a column name in the dataframe
print("\nSelect your second filter: ")
for i, str in enumerate(nameSubset):
    print("\t{0}".format(str))
crit2 = input()
crit2 = crit2.strip()
crit2Valid = False
while (crit2Valid == False):
    if (crit2 in names[nameStart:nameEnd]):
        crit2Valid = True
    else:
        crit2 = input("Error: Please select a valid criteria: ")

# Choose whether to filter by high or low amount
sort2 = input("\nWould you like high or low {0}?\n\tHigh\n\tLow\n".format(crit2))
sort2 = sort2.replace(" ", "")
sort2Valid = False
while (sort2Valid == False):
    if (sort2 == "High" or sort2 == "Low"):
        # print("True\n")
        sort2Valid = True
    else:
        sort2 = input("Error: Please select 'High' or 'Low': ")

# Remove space from user input in order to access dataframe
# Extract only the data relevant to the criterion.
# Find the upper and lower quantile of that data.
# If user selected "High":  filter dataframe to include only entries with values of the criterion greater than or equal to the 0.75 quantile
# If user selected "Low":   filter dataframe to include only entries with values of the crtierion less than or equal to the 0.25 quantile
# Print the resulting dataframe
crit2 = crit2.replace(" ", "")
df_sub2 = df[crit2]
try:
    q_df = df_sub2.quantile([.25, .75])
except TypeError:
    quitProgram("Non-integer value in {0}".format(crit2))
if (sort2 == "High"):
    df = df.query("{0} >= {1}".format(crit2, q_df[0.75]))
    df = df.sort_values(by=crit2, ascending=False)
    print(df)
elif (sort2 == "Low"):
    df = df.query("{0} <= {1}".format(crit2, q_df[0.25]))
    df = df.sort_values(by=crit2, ascending=True)
    print(df)

print("\n")