#/usr/bin/python

import csv, json
import pandas as pandasForSortingCSV

#csvFilePath = "jlab-eda_20APR23.csv"
FilePath = "syft-grype.json"

jsonFilePath = "Emass_api_json_format.txt"

#Read the csv and add the data to a dictionary

data = {}
with open(FilePath, 'r') as f:
    data = json.load(f)
    
    print(data)
#Write data to a root node.....
root={}
root["benchmark"] = data


#Write data to a json file
with open(jsonFilePath, "w") as jsonFile:
    
    jsonFile.write(json.dumps(root, indent=4))




