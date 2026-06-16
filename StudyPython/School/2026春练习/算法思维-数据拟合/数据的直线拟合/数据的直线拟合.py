import numpy as np
XY=np.genfromtxt('XY1.csv',skip_header = 1,delimiter=',',usecols=(1,2))#样本点文件
X=XY[:,0]#样本点的x坐标值
Y=XY[:,1]#样本点的y坐标值
lr=eval(input('请输入学习率:'))
rounds=eval(input('请输入对数据集的迭代轮数:'))
w=np.array(eval(input('请输入初始权重值:')))

#请用批量梯度下降法迭代更新w值，找到最佳拟合直线
########################begin########################
X_b = np.c_[np.ones((len(X), 1)), X] # 数组拼接

# 确保 w 是列向量以便进行矩阵运算
w = w.reshape(-1, 1)
Y = Y.reshape(-1, 1)

# 获取样本数量 m
m = len(X)

# 2. 开始迭代更新
for i in range(rounds):
    # 计算预测值 h = X_b * w
    h = X_b.dot(w)

    # 计算误差向量 errors = h - y
    errors = h - Y

    # 计算梯度: gradient = (1/m) * X_b^T * errors
    # X_b.T 是转置操作
    gradient = (1.0 / m) * X_b.T.dot(errors)

    # 更新权重 w = w - lr * gradient
    w = w - lr * gradient

# 3. 迭代结束，计算最终结果并输出
# 计算最终的预测值和误差
final_h = X_b.dot(w)
final_errors = final_h - Y

# 计算均方误差 MSE = (1/m) * sum(errors^2)
mse = (1.0 / m) * np.sum(final_errors ** 2)

# 提取 w0 和 w1
w0 = w[0][0]
w1 = w[1][0]

# 按要求保留6位小数输出
print("最优参数: w0=%.6f, w1=%.6f, mse=%.6f" % (w0, w1, mse))
###########################end##########################