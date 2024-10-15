from sklearn.datasets import load_iris
from sklearn import tree
import pandas as pd


file_path = 'pre_processing1.csv'  # 替换为你的文件路径
df = pd.read_csv(file_path)
label = df.loc[:,'是否脑卒中']
label.to_csv('targets.csv',index=False)
target = label.values.tolist()
# print(target)
iris = load_iris()
print(iris.data)
print(iris.target)
labels = df.columns.tolist()
labels.remove('是否脑卒中')
# a = iris['feature_names']
# print(a)
# print(labels)