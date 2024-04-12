datasetDict = {}
with open("HKS2023.csv", "r") as inputFile:
    tempList = inputFile.readlines()
    for item in tempList[0].split(","):
        datasetDict[item.replace('"', "")] = []

    print(datasetDict)

    for row in tempList[1:]:
        for i in range(len(row.split(","))-1):
            datasetDict[list(datasetDict.keys())[i]].append(row.split(",")[i].replace('"', ""))