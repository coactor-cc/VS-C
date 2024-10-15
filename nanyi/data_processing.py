import pandas as pd
import numpy as np

# 读取 CSV 文件
file_path = 'Sheet2.csv'  # 替换为你的文件路径
file_path_target = 'targets.csv'
df = pd.read_csv(file_path)
#
# 输出 DataFrame
# 删除更改某一列
df.drop(columns=['性别'], inplace=True)
df.drop(columns=['吸烟情况'], inplace=True)
df.drop(columns=['饮酒情况'], inplace=True)
df.drop(columns=['运动情况'], inplace=True)
df.drop(columns=['吸烟饮酒和运动赋分总分'], inplace=True)
# df.drop(columns=['空腹血糖7.0'], inplace=True)
df.drop(columns=['1：＜7.0（正常）  2：≥7.0（高血糖）'], inplace=True)
# df.drop(columns=['总胆固醇TC6.2'], inplace=True)
df.drop(columns=['1：＜6.2（正常）  2：≥6.2（异常）'], inplace=True)
# df.drop(columns=['甘油三脂TG2.3'], inplace=True)
df.drop(columns=['1：＜2.3  （正常）2：≥2.3（异常）'], inplace=True)
# df.drop(columns=['高密度脂蛋白1.0'], inplace=True)
df.drop(columns=['1：≥1（正常）  2：＜1（异常）'], inplace=True)
# df.drop(columns=['低密度脂蛋白4.1'], inplace=True)
df.drop(columns=['1：＜4.1（正常）  2：≥4.1（异常）'], inplace=True)
# df.drop(columns=['收缩压SBP'], inplace=True)
# df.drop(columns=['是否高脂血症的总体评价 1：正常血脂  2：异常血脂'], inplace=True)
# df.drop(columns=['舒张压DBP'], inplace=True)
df.drop(columns=['1：正常血压  2：高血压'], inplace=True)
df.drop(columns=['慢性非传染性疾病诊断'], inplace=True)
target = pd.read_csv('targets.csv')
df['是否脑卒中'] = target
# df.to_csv('continuous_processing.csv', index=False)
# file_path = 'continuous_processing.csv'
# df = pd.read_csv(file_path)

df.drop(columns=['腰围'], inplace=True)
df.to_csv('continuous_processing.csv', index=False)
# print(df)
# 将数据保存到列表中（如果需要）
# data_list = df.values.tolist()
# print(data_list)
# df.drop(columns=['column_name'], inplace=True)
# df.rename(columns={'old_column_name': 'new_column_name'}, inplace=True)

# file_path = 'pre_processing.csv'  # 替换为你的文件路径
# df = pd.read_csv(file_path)
# # print(df.loc[:,'慢性非传染性疾病诊断'])
# result = df.loc[:,'慢性非传染性疾病诊断']
# data_list = result.values.tolist()
# empty_list = [0]*len(data_list)
# # print(empty_list)
# for x in range(len(data_list)):
#     data_list[x] = str(data_list[x])
#     if '脑卒中' in data_list[x]:
#         empty_list[x] = 1
# df['是否脑卒中'] = empty_list
# df.drop(columns=['慢性非传染性疾病诊断'], inplace=True)
# df.to_csv('pre_processing1.csv')

# file_path = 'pre_processing1.csv'  # 替换为你的文件路径
# file_path_targets = 'targets.csv'
# df = pd.read_csv(file_path)
# df_targets = pd.read_csv(file_path_targets)
# df.drop(columns=['Unnamed: 0'], inplace=True)
# df.drop(columns=['BMI'], inplace=True)
# df.drop(columns=['年龄'], inplace=True)
# df.drop(columns=['腰围'], inplace=True)
# label = df.columns.tolist()
# label.remove('是否脑卒中')
# print(labels)
# sys.exit()
# df.drop(columns=['是否脑卒中'], inplace=True)
# df.to_csv('mission2.csv', index=False)
