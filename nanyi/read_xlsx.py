
import pandas as pd

# 读取 Excel 文件
file_path = 'Sheet2.xlsx'  # 替换为你的文件路径
df = pd.read_excel(file_path, sheet_name='Sheet1')

data_list = df.values.tolist()
output_df = pd.DataFrame(data_list, columns=df.columns)
# 保存为 CSV 文件
output_csv_file = 'Sheet2.csv'  # 输出文件名
output_df.to_csv(output_csv_file, index=False)