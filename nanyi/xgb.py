from sklearn.datasets import load_svmlight_file
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
import mglearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split


xgbc = XGBClassifier(max_depth=2,
                     learning_rate=1,
                     n_estimators=2, # number of iterations or number of trees
                     slient=0,
                     objective="binary:logistic"
                    )

def create_dataset():
    file_path = 'pre_processing1.csv'  # 替换为你的文件路径
    file_path_targets = 'targets.csv'
    df = pd.read_csv(file_path)
    df_targets = pd.read_csv(file_path_targets)
    df.drop(columns=['Unnamed: 0'], inplace=True)
    df.drop(columns=['BMI'], inplace=True)
    df.drop(columns=['年龄'], inplace=True)
    df.drop(columns=['腰围'], inplace=True)
    label = df.columns.tolist()
    label.remove('是否脑卒中')
    # print(labels)
    # sys.exit()
    df.drop(columns=['是否脑卒中'], inplace=True)
    data_list = df.values.tolist()
    data = np.array(data_list)
    target = df_targets.values.tolist()
    target_1d = []
    for i in range(len(target)):
        target_1d.append(target[i][0])
    target = np.array(target_1d)
    label = np.array(label)
    return data, target, label

datas, targets, labels = create_dataset()
# X, y = make_moons(n_samples=100, noise=0.25, random_state=3)
X = datas
# print(X)
y = targets
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

xgbc.fit(X_train, y_train)

pred_train = xgbc.predict(X_train)
pred_train = [round(x) for x in pred_train]
num = 0
print(len(pred_train))
# for j in y_train:
#     if j == 1:
#         num += 1
# print(num)
# for i in pred_train:
#     if i == 1:
#         num += 1
# print(num)
train_score = accuracy_score(y_train, pred_train)
print("Train Accuracy: %.2f%%" % (train_score * 100))

pred_test = xgbc.predict(X_test)
pred_test = [1 if x >= 0.5 else 0 for x in pred_test]
print("Test Accuracy: %.2f%%" % (accuracy_score(y_test, pred_test) * 100))