import pandas as pandasForSortingCSV

csvData = pandasForSortingCSV.read_csv('small.csv')
print ("\nBefore Sorinting:")
print(csvData[:20])

csvData.sort_values(["Severity"], axis=0,ascending=[True],inplace=True)
print ("\nAfter Sorinting:")
print(csvData[:20])


