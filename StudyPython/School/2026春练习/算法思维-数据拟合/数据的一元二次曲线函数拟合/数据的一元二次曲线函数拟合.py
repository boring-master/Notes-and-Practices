import numpy as np
seed=eval(input('请输入随机种子:'))
np.random.seed(seed)
w=np.random.randn(3) #初始化二次函数的参数
learning_rate=eval(input('请输入学习率:'))
roundN=eval(input('请输入对数据集学习的轮数:'))
XY=np.genfromtxt('XY2.csv',skip_header = 1,delimiter=',',usecols=(1,2))#数据文件，存放样本点，包含x,y值
X=XY[:,0]
Y=XY[:,1]

#请用批量梯度下降法对误差进行最小化迭代，从而求出样本点的拟合曲线函数
#####################begin###################
X_poly = np.column_stack([np.ones(len(X)), X, X ** 2])
m = len(Y)
for epoch in range(roundN):
    y_hat = X_poly.dot(w)
    error = y_hat - Y
    grad = (X_poly.T.dot(error)) / m
    w = w - learning_rate * grad
y_hat = X_poly.dot(w)
mse = np.mean((y_hat - Y) ** 2)
print(f"w0={w[0]:.6f},w1={w[1]:.6f},w2={w[2]:.6f},mse={mse:.6f}")
######################end###################