# "literal_eval" is a more secure alternative to eval that fits my needs.
from ast import literal_eval

# Creates a dictionary for adding the dataset in.
# This is how the formating will end up:
# 
# "x", "y", "z"
# example1, example2, example3                  ---->     datasetDict = {"x": [example1, placeholder1], "y": [example2, placeholder2], "z": [example3, placeholder3]}
# placeholder1, placeholder2, placeholder 3
# 
datasetDict = {}

# Opens the csv file in a "with open" clause, automatically closing the connection when completing.
with open("HKS2023.csv", "r") as inputFile:
    # "inputFile" gets wiped after being read by the code, so it needs to be copied over to a temporary list.
    tempList = inputFile.readlines()

    # Creates the first row's items as keys connected to empty lists in the "datasetDict" dictionary.
    for item in literal_eval(f"[{tempList[0]}]"):
        datasetDict[item] = []

    # Appends the items in the other rows to their respective key.
    for row in tempList[1:]:
        row = literal_eval(f"[{row}]")
        for i in range(len(literal_eval(f"[{tempList[0]}]"))-1):
            datasetDict[list(datasetDict.keys())[i]].append(row[i])

# Sorting by number
tempList = sorted(datasetDict["Bib"], reverse=True)
print(tempList[:3])

# Collecting all the non-binary people(?)
nonBinaryPeeps = []
for i in range(len(datasetDict["Gender"])):
    if datasetDict["Gender"][i] == "N":
        nonBinaryPeeps.append(datasetDict["Firstname"][i])
print(nonBinaryPeeps)