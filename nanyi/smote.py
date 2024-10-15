# 引入三方库
import pandas as pd
from imblearn.over_sampling import SMOTE
# 数据预处理
data = pd.read_csv("continuous_processing.csv")
# print(data.dtypes)
# data.drop(columns=['BMI'], inplace=True)
X_train, y_train = data.iloc[:, :-1], data.iloc[:, -1]
counts_1 = y_train.value_counts()
# # # print('不平衡数据分布情况为')
# print(counts_1)
smt = SMOTE()
X_train_sm, y_train_sm = smt.fit_resample(X_train, y_train)
counts_sm = y_train_sm.value_counts()
# print('SMOTE（输出为data_smote）平衡数据计数')
# print(counts_sm)
data_sm = pd.concat([X_train_sm, y_train_sm], axis=1)
data_sm.to_csv('continuous_data_smote.csv', index=False)
data = pd.read_csv("continuous_data_smote.csv")
targets = data.loc[:,'是否脑卒中']
targets.to_csv('continuous_targets_smote.csv',index=False)
data.drop(columns=['是否脑卒中'], inplace=True)
data.to_csv("continuous_data_smote.csv", index=False)
