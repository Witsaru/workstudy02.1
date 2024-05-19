import csv
import numpy as np
import pandas as pd

# Read the CSV file
with open('csv_data/Test_02/Left_Test_02_4.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Extract the data, filtering out unrealistic values
x = []
y = []
for row in data[1:]:
    index = int(row[0])
    value = float(row[1])
    # print(row[1::])
    # if value < 100:  # Filter out values greater than 100 (adjust threshold as needed)
        # x.append(index)
    y.append(row[1::])
print(len(y),end=('\t'))
with open('csv_data/Test_02/Left_Test_02_8.csv', 'r') as file:
    reader2 = csv.reader(file)
    data2 = list(reader2)

# print(data2)

for row in data2[1:]:
    # print(float(row[1]))
    value = float(row[1])
    y.append(row[1::])

print(len(y))
np_ = np.array(y)
df = pd.DataFrame(np_)
df.to_csv('re_build_csv.csv')