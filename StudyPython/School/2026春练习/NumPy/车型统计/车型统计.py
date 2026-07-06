import numpy as np
sales = np.array(eval(input())) # 数据录入
cars = ['轿车','SUV','MPV','跑车','皮卡'] # 车型
# 1. 车型年度统计:计算每个车型的全年总销量及每个车型的平均季度销量(保留1位小数)，得到两个形状为 (5,) 的数组 model_total 和 model_avg
model_total = np.sum(sales,axis=1)           # 按行求和，shape (5,)
model_avg = np.mean(sales,axis=1)             # 按行求平均，shape (5,)
# 2. 季度销售趋势：计算每个季度的所有车型总销量，输出形状为 (4,) 的数组 quarter_total。
quarter_total = np.sum(sales,axis=0)
# 3. 明星车型：找出每个季度的明星车型，即每个季度销量最高的车型。
max_indices = np.argmax(sales, axis=0)
max_sales = [cars[i] for i in max_indices]
#  4. 低销量预警：找出每个季度的最低销量车型，即每个季度销量最低的车型。
min_indices = np.argmin(sales, axis=0)
min_sales = [cars[i] for i in min_indices]
# 输出结果
print("车型总销量:", model_total)
print("车型平均季度销量:", model_avg)
print("各季度总销量:", quarter_total)
print(f"各季度明星车型: {max_sales} ")
print(f"各季度最低销量车型: {min_sales} ")