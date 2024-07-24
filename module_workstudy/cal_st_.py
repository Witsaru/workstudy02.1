import math
import csv
import numpy as np

def calcu_stantime(file_,ratfac,allowa):

    with open(file_, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

        x = []
        y = []

    for row in data[1:]:
        index = int(row[0])
        value = float(row[2])
        if value < 100:  # Filter out values greater than 100 (adjust threshold as needed)
            x.append(index)
            y.append(value)

    y_np = np.array(y)
    aver = round(sum(y_np)/len(y_np),3)

    #calculate interquartile range 
    q3, q1 = np.percentile(y_np, [75 ,25])
    iqr = q3 - q1

    iqr_y = []
    for i in y_np:
        if i < q1-(iqr*1.5):
            iqr_y.append(aver)
        
        elif i > q3 + (iqr*1.5):
            iqr_y.append(aver)

        else:
            iqr_y.append(i)

    aver = round(sum(iqr_y)/len(iqr_y),3)
    nor = round(aver*(ratfac/100),3)
    sta = round(nor * (1+(allowa/100)),3)

    return [aver, nor, sta]

if __name__ == "__main__":
    st = calcu_stantime('csv_data/R_test_01_A/real_Mix_R_test_01_A_1.csv',60,15)
    print(st)