# Reading CSV File Using Pandas
curl -O https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/data/weight-height.csv

import pandas as pd

df = pd.read_csv('weight-height.csv')
print(df)

# Get the first five rows
print(df.head()) # give five rows we can increase the number of rows by passing argument to the head() method
	Gender	Height	Weight
0	Male	73.847017	241.893563
1	Male	68.781904	162.310473
2	Male	74.110105	212.740856
3	Male	71.730978	220.042470
4	Male	69.881796	206.349801

# Get the last fivr rows
print(df.tail()) # tails give the last five rows, we can increase the rows by passing argument to tail method
	Gender	Height	Weight
9995	Female	66.172652	136.777454
9996	Female	67.067155	170.867906
9997	Female	63.867992	128.475319
9998	Female	69.034243	163.852461
9999	Female	61.944246	113.649103

# Get the title column as pandas series
print(df.shape) # as you can see 10000 rows and three columns
(10000, 3)
print(df.columns)
Index(['Gender', 'Height', 'Weight'], dtype='object')
heights = df['Height'] # this is now a series

print(heights)

    0       73.847017
    1       68.781904
    2       74.110105
    3       71.730978
    4       69.881796
              ...    
    9995    66.172652
    9996    67.067155
    9997    63.867992
    9998    69.034243
    9999    61.944246
    Name: Height, Length: 10000, dtype: float64

weights = df['Weight'] # this is now a series
print(weights)

    0       241.893563
    1       162.310473
    2       212.740856
    3       220.042470
    4       206.349801
               ...    
    9995    136.777454
    9996    170.867906
    9997    128.475319
    9998    163.852461
    9999    113.649103
    Name: Weight, Length: 10000, dtype: float64
print(len(heights) == len(weights))
True

# Count the number of rows and columns
In [16]: class_23 = titanic[titanic["Pclass"].isin([2, 3])]

In [17]: class_23.head()
Out[17]:
 PassengerId   Survived Pclass  ...    Fare  Cabin   Embarked
0          1          0      3  ...   7.2500   NaN          S
2          3          1      3  ...   7.9250   NaN          S
4          5          0      3  ...   8.0500   NaN          S
5          6          0      3  ...   8.4583   NaN          Q
7          8          0      3  ...   21.0750  NaN          S

[5 rows * 12 columns]

# Filter the titles which contain python
item = []
for w in word:
       for line in item:
              if w in line:
                     j=Python.replace(it,'JavaScript')
                     item.append(j)

# Filter the titles which contain JavaScript
item = []
for w in word:
       for line item:
              if w in line:
              j=JavaScript.replace(it,'Python')
       item.append(j) 