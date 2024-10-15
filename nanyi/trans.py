import pandas as pd

file_path = 'continuous_data_smote.csv'  # 替换为你的文件路径
file_path_target = 'continuous_targets_smote.csv'
# df = pd.read_csv('Sheet2.csv')
data = pd.read_csv(file_path)
label = data.columns.tolist()
# print(label)
temp = []
def panding(label1, num, label2):
    temp = []
    for x in data[label1]:
        if x < num:
            temp.append(0)
        if x >= num:
            temp.append(1)
    data[label2] = temp
panding('空腹血糖7.0', 7.0, '是否高血糖')
panding('总胆固醇TC6.2', 6.2, '是否高胆固醇')
panding('甘油三脂TG2.3', 2.3, '是否高甘油三脂')
temp = []
for x in data['高密度脂蛋白1.0']:
    if x < 1.0:
        temp.append(1)
    if x >= 1.0:
        temp.append(0)
data['是否正常高密度脂蛋白'] = temp
panding('低密度脂蛋白4.1', 4.1, '是否正常低密度脂蛋白')
# print(data)
data.drop(columns=['空腹血糖7.0'], inplace=True)
data.drop(columns=['总胆固醇TC6.2'], inplace=True)
data.drop(columns=['甘油三脂TG2.3'], inplace=True)
data.drop(columns=['高密度脂蛋白1.0'], inplace=True)
data.drop(columns=['低密度脂蛋白4.1'], inplace=True)
data.to_csv('discrete_data_smote.csv', index=False)