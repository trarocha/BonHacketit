# Tracy Rocha
# Bon Hacketit
import pandas as pd
import re

def openFile(res):
    res = res.replace(" ", "")
    filename = "%s.csv" % res
    try: 
        df = pd.read_csv(filename, sep=',', header=0)
    except FileNotFoundError:
        return 0
    return df

def getNames(names):
    for i, str in enumerate(names):
        names[i] = re.sub('([A-Z])', r' \1', str)
        names[i] = names[i].lstrip()
    return names