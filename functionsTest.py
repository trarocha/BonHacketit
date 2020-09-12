# Tracy Rocha
# Bon Hacketit 2020
# Narrow It Down
# Test Harness for functions.py

from functions import openFile, getNames

# Initiate counter
passed = 0
tests = 0

# openFile()
print("\n# Testing openFile() #")
df = openFile("Not a File")
if df == 0:
    print("\tError successfully caught")
    passed += 1
else:
    print("\tFailed to catch error")
tests += 1
df = openFile("Panda Express")
if df.shape != (0, 0):
    print("\tFile successfully opened")
    passed += 1
else:
    print("\tFiled failed to open")
tests += 1

# getNames()
print("\n# Testing getNames() #")
tests += 1
names = list(df)
names = getNames(names)
# print(names)
if (names[0] == "Food") & (names[5] == "Total Fat"):
    print("\tNames successfully assigned")
    passed += 1
else:
    print("\tFailed to assign names")
    print("\t\tExpected: ' Food', Actual: {0}".format(names[0]))
    print("\t\tExpected: ' Total Fat', Actual: {0}".format(names[5]))

# Final results
print("\n# Final Results #\n\tPassed {0} out of {1} tests\n".format(passed, tests))