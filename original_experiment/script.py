import arff, numpy as np
import random
import pandas as pd
ARFF_NAME = 'dataset_57_hypothyroid.arff'
CSV_NAME = 'dataset_converted.csv'
PREFIX = 'out/'


# generates missing values randomly distributed across all attributes
# C1 a
def randomGenerateMissingValues(values, percent):
    # create a copy
    mat = values.copy()
    # number of values to replace
    prop = int(mat.size * percent)
    # indices to mask
    mask = random.sample(range(mat.size), prop)
    # replace with ?
    np.put(mat, mask, '?')

    return mat

# generates missing values across specific attribute (with attributeIndex)
# C1 b
def generateMissingValuesForAttribute(values, percent, attributeIndex):
    # create a copy
    mat = values.copy()
    column = values[:,attributeIndex].copy()
    # number of values to replace
    prop = int(column.size * percent)
    # indices to mask
    mask = random.sample(range(column.size), prop)
    # replace with Na
    np.put(column, mask, '?')

    mat[:,attributeIndex] = column;

    return mat    

# function for converting arff content to csv file
def toCsv(content):
    data = False
    header = ""
    newContent = []
    for line in content:
        if not data:
            if "@attribute" in line:
                attri = line.split()
                columnName = attri[attri.index("@attribute")+1]
                header = header + columnName + ","
            elif "@data" in line:
                data = True
                header = header[:-1]
                header += '\n'
                newContent.append(header)
        else:
            newContent.append(line)
    return newContent

#convert arff to csv 
with open(ARFF_NAME , "r") as inFile:
        content = inFile.readlines()
        new = toCsv(content)
        with open(CSV_NAME, "w") as outFile:
            outFile.writelines(new)     

#open new csv     
df=pd.read_csv(CSV_NAME, sep=',')


#create new datasets and save to csv
#C 2.a
ds1 = pd.DataFrame(generateMissingValuesForAttribute(df.values,0.1,18),columns= df.columns)
ds1.to_csv(PREFIX + 'missing_values_Attr19_P10.csv', sep=',', index=False)
ds2 = pd.DataFrame(generateMissingValuesForAttribute(df.values,0.8,18),columns= df.columns)
ds2.to_csv(PREFIX + 'missing_values_Attr19_P80.csv', sep=',', index=False)
ds3 = pd.DataFrame(generateMissingValuesForAttribute(df.values,0.1,17),columns= df.columns)
ds3.to_csv(PREFIX + 'missing_values_Attr18_P10.csv', sep=',', index=False)
ds4 = pd.DataFrame(generateMissingValuesForAttribute(df.values,0.8,17),columns= df.columns)
ds4.to_csv(PREFIX + 'missing_values_Attr18_P80.csv', sep=',', index=False)
#C 2.b
ds5 = pd.DataFrame(randomGenerateMissingValues(df.values,0.1),columns= df.columns)
ds5.to_csv(PREFIX + 'missing_values_Overall_P10.csv', sep=',', index=False)
ds6 = pd.DataFrame(randomGenerateMissingValues(df.values,0.8),columns= df.columns)
ds6.to_csv(PREFIX + 'missing_values_Overall_P80.csv', sep=',', index=False)



