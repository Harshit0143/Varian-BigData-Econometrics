#!/usr/bin/env python3
import pandas as pd
import numpy as np
filename = './113925-V1/ml-data/Titanic/titanic3.csv'
df = pd.read_csv(filename)
print(df.head())
print(df.columns)
print("Median: " , df['age'].median())
print("Mean: " , df['age'].mean())

def value(age):
    val = -0.002 * age + 0.465
    return 1 / (1 + np.exp(-val))

print("min age:" , df['age'].min() , "val:" , value(df['age'].min()))
print("max age:" , df['age'].max() , "val:" , value(df['age'].max()))
