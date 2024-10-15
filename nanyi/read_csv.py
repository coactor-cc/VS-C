import pandas as pd
import numpy as np

file_path = 'pre_processing1.csv'  # 替换为你的文件路径
df = pd.read_csv(file_path)
# df = df.loc[:, df.columns.notnull()]
df.drop(columns=['Unnamed: 0'], inplace=True)
df.drop(columns=['BMI'], inplace=True)
df.drop(columns=['年龄'], inplace=True)
df.drop(columns=['腰围'], inplace=True)
labels = df.columns.tolist()
labels.remove('是否脑卒中')
print(labels)
# print(df)
data_list = df.values.tolist()
# print(data_list)
# print(data_list)