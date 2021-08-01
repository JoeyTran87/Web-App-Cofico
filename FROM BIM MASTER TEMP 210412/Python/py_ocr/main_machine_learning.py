# SOLOLREARN
import numpy as np
import pandas as pd


#GLOBAL VAR

df = None


def basic_statitics():
    ages = [15, 16, 18, 19, 22, 24, 29, 30, 34 ]
    print(f"DATA AGE: {ages}")

    # 1. MEAN
    print(f"MEAN: {np.mean(ages)}")

    # 2.MEDIAN
    print(f"MEDIAN: {np.median(ages)}")

    # 2.1 PECENTILE : MEDIAN = PERCENTILE 20%
    print(f"25th PERCENTILE: {np.percentile(ages,25)}")
    print(f"50th PERCENTILE = MEDIAN: {np.percentile(ages,50)}")
    print(f"75th PERCENTILE: {np.percentile(ages,75)}")
    print(f"MEAN: {np.mean(ages)}")

    # 3. VARIANCE = PHƯƠNG SAI
    print(f"VARIANCE: {np.var(ages)}")

    # 4. STANDARD DEVIATION 
    print(f"STANDARD DEVIATION: {np.std(ages)}")

def basic_use_pandas():
    global df
    # 1. READ DATA CSV
    df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
    # print(df.head())
    # print(df.describe())
    # 2. READ COLUMN
    col = df['Fare']
    # print(col)
    # 3. READ MULTI COLUMN
    small_df = df[['Age', 'Sex', 'Survived']]
    # print(small_df.head())
    # 4. CREATE NEW COLUMN
    df['male'] = df['Sex'] == 'male'
    df['female'] = df['Sex'] == 'female'
    # print(df.head())

basic_use_pandas()
# 1. DATAFRAME to NUMPY Array
# print(f"DATA FRAME VALUE: {df['Fare'].values}")
arr = df[['Pclass','Fare','Age']]
print(f"DATA FRAME VALUES: {arr.values}")
print(f"DATA FRAME VALUES SHAPE: {arr.shape}")


