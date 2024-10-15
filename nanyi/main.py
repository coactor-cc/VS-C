'''
随机上采样（Random Oversampling）
随机上采样是指对少数类样本进行复制，使得样本数量与多数类样本数量相等。
下面是使用Python的imbalanced-learn库进行随机上采样的示例代码：
X和y分别表示原始的特征矩阵和标签向量，fit_resample()方法将进行随机上采样操作。
'''
from imblearn.over_sampling import RandomOverSampler
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import sys
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split


def create_dataset():
    file_path = 'discrete_data_smote.csv'  # 替换为你的文件路径
    file_path_targets = 'continuous_targets_smote.csv'
    df = pd.read_csv(file_path)
    df_targets = pd.read_csv(file_path_targets)
    label = df.columns.tolist()
    data_list = df.values.tolist()
    data = np.array(data_list)
    target = df_targets.values.tolist()
    target_1d = []
    for i in range(len(target)):
        target_1d.append(target[i][0])
    target = np.array(target_1d)
    # label = np.array(label)
    return data, target, label
X,y,a = create_dataset()
# print(X.shape)
# print(X.shape)
# y = pd.DataFrame(y, columns=['是否脑卒中'])
# print(y)
# print(y.value_counts())
# ros = RandomOverSampler(random_state=42)
# X_resampled, y_resampled = ros.fit_resample(X, y)
# y_resampled = np.array(y_resampled)
# temp = []
# for i in range(len(y_resampled)):
#     temp.append(y_resampled[i][0])
# temp = np.array(temp)
# # # print(temp)
# y_resampled = temp
# print(y_resampled)
# print(X_resampled.shape)
# 拆分为训练集和临时集（包含验证集和测试集）
X_train, X_test_temp, y_train, y_test_temp = train_test_split(X, y, stratify=y, random_state=42)
X_test, X_valid, y_test, y_valid = train_test_split(X_test_temp, y_test_temp, stratify=y_test_temp, random_state=42)
print(X_train.shape)
print(X_test.shape)
print(X_valid.shape)
# print(X_train.shape)
# sys.exit()
# print(y_valid)
# sys.exit()
forest = RandomForestClassifier(n_estimators=5, random_state=2, class_weight={0:1.0,1:1.0})
forest.fit(X_train, y_train)
pred_target = forest.predict(X_valid)
# print(y_valid)
# print(pred_target)
num1,num2,num3 = 0,0,0
a,b = [],[]
for i in range(len(pred_target)):
    if pred_target[i] == 1:
        a.append(i)
        num1 += 1
print(num1)
# print(a)
for j in range(len(y_valid)):
    if y_valid[j] == 1:
        b.append(j)
        num2 += 1
print(num2)
# print(b)
for k in a:
    if k in b:
        num3 += 1
print(num3)
print("Accuracy on training set: {:.3f}".format(forest.score(X_train, y_train)))
print("Accuracy on test set: {:.3f}".format(forest.score(X_test, y_test)))
print("Accuracy on validation set: {:.3f}".format(forest.score(X_valid, y_valid)))


