# Tracy Rocha
# Bon Hacketit 2020
# Narrow It Down
# Contains functions for opening and processing CSV files

import pandas as pd
import re

# Input: string
# Output: dataframe
# Takes in a string and returns a csv file of the same name.
# Requirements: Existence of csv file with the name indicated by the string.
#               CSV file should be in camelcase (i.e. PandaExpress)
# If no such file exists, function returns 0.
def openFile(res):
    res = res.replace(" ", "")                          # Remove spaces from input
    filename = "%s.csv" % res                           # Create file name using input string
    try: 
        df = pd.read_csv(filename, sep=',', header=0)   # Open file
    except FileNotFoundError:
        return (0, 0)
    return df

# Input: list
# Output: list
# Takes in a list of strings and returns the same list with spaces between words
#   i.e. ['ServingSize', 'CaloriesFromFat'] becomes ['Serving Size', 'Calories From Fat']
# Requirements: List items should be strings in camelcase.
def getNames(names):
    for i, str in enumerate(names):
        names[i] = re.sub('([A-Z])', r' \1', str)   # Add a space in front of each capital letter
        names[i] = names[i].lstrip()                # Remove leading space
    return names