import csv
import pandas as pd
import numpy as np
import re
i=[]
i2 = [float(x) for x in i]
with open('opads.csv', 'r') as f:
    reader = csv.reader(f)
    
    for line in reader:
        
        i.append(line)
        
k1=pd.read_table('opads.csv', header=None)
aver1=k1.mean()
#aver=(re.sub(r'\bdtype: float64\b', '', aver1, flags=re.IGNORECASE) )
#if i>=aver in k1:
  #  print(i)
#with open('opads.csv', 'r') as f:
    #reader = csv.DictReader(f,delimiter=";")
    #for row in reader:
        #while float(row['op']) > i:
           # i = float(row['op'])
        #while float(row['op']) < b:
            #b = float(row['op'])
    
       # print('День', row['d'], 'Опади', row['op'])
print(line)
print(i)

