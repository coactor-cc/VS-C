import mglearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split

def create_dataset():
    file_path = 'data_smote.csv'  # 替换为你的文件路径
    file_path_targets = 'targets_smote.csv'
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
    label = np.array(label)
    return data, target, label

datas, targets, labels = create_dataset()
# X, y = make_moons(n_samples=100, noise=0.25, random_state=3)
X = datas
# print(X)
y = targets
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
# print(X_train.shape)
# sys.exit()

forest = RandomForestClassifier(n_estimators=5, random_state=2, class_weight={0:1.0,1:10.0})
forest.fit(X_train, y_train)
pred_target = forest.predict(X_train)
num1,num2,num3 = 0,0,0
a,b = [],[]
for i in range(len(pred_target)):
    if pred_target[i] == 1:
        a.append(i)
        num1 += 1
print(num1)
for j in range(len(y_train)):
    if y_train[j] == 1:
        b.append(j)
        num2 += 1
print(num2)
for k in a:
    if k in b:
        num3 += 1
print(num3)
print("Accuracy on training set: {:.3f}".format(forest.score(X_train, y_train)))
print("Accuracy on test set: {:.3f}".format(forest.score(X_test, y_test)))

#
#
# from sklearn.datasets import load_breast_cancer
#
# cancer = load_breast_cancer()
#
# X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=0)
# forest = RandomForestClassifier(n_estimators=100, random_state=0)
# forest.fit(X_train, y_train)
#
# print("Accuracy on training set: {:.3f}".format(forest.score(X_train, y_train)))
# print("Accuracy on test set: {:.3f}".format(forest.score(X_test, y_test)))
#
#
# def plot_feature_importances_cancer(model):
#     n_features = cancer.data.shape[1]
#     plt.barh(range(n_features), model.feature_importances_, align='center')
#     plt.yticks(np.arange(n_features), cancer.feature_names)
#     plt.xlabel("Feature importance")
#     plt.ylabel("Feature")
#
# plot_feature_importances_cancer(forest)
