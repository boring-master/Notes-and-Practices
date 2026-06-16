import numpy as np
seed=eval(input('请输入随机数种子:'))
np.random.seed(seed)
data=np.genfromtxt('Folds5x2_pp.csv',skip_header = 1,delimiter=',',usecols=(1,2,3,4,5))
np.random.shuffle(data)  #随机打乱examples
data=data[0:2000,:]  #为节约时间，仅取2000个样本进行训练和评估
X=data[:,0:-1]
X=(X-X.min(axis=0))/(X.max(axis=0)-X.min(axis=0)) #归一化
y=data[:,-1]

#训练集测试集划分
testRate=0.2 #测试集的占比
X_test=X[0:int(len(X)*testRate)] #按比例划分训练集和测试集
y_test=y[0:int(len(X)*testRate)].reshape(-1,1)
X_train=X[int(len(X)*testRate):]
y_train=y[int(len(X)*testRate):].reshape(-1,1)

# 网络初始化
input_size = X.shape[1]
hidden_size = int(input('请录入隐藏层神经元个数:'))
output_size = 1
W1 = np.random.randn(hidden_size, input_size)    # (J,n)
b1 = np.zeros(hidden_size)                       # (J,)
W2 = np.random.randn(output_size, hidden_size)   # (1,J)
b2 = np.zeros(output_size)                       # 标量

#  激活函数
def tanh(z):
    return np.tanh(z)
def tanh_derivative(z):
    return 1 - tanh(z)**2

#  训练参数
epochs = int(input('请录入训练轮数:'))
learning_rate = float(input('请录入学习率:'))
m = len(X_train)

###################请开始你的训练及评估########################

for i in range(epochs):
    # 前向传播
    Z = X_train @ W1.T + b1          # (m, hidden_size)
    A = tanh(Z)                       # (m, hidden_size)
    y_pred = A @ W2.T + b2            # (m, 1)

    # 反向传播
    delta2 = (y_pred - y_train) / m   # (m, 1)
    dw2 = delta2.T @ A                 # (1, hidden_size)
    db2 = np.sum(delta2, axis=0)       # (1,)

    delta1 = (delta2 @ W2) * tanh_derivative(Z)  # (m, hidden_size)
    dw1 = delta1.T @ X_train           # (hidden_size, input_size)
    db1 = np.sum(delta1, axis=0)       # (hidden_size,)

    # 更新参数
    W2 = W2 - learning_rate * dw2
    b2 = b2 - learning_rate * db2
    W1 = W1 - learning_rate * dw1
    b1 = b1 - learning_rate * db1

# 训练集评估
Z_train = X_train @ W1.T + b1
A_train = tanh(Z_train)
y_train_pred = A_train @ W2.T + b2
train_mse = np.mean((y_train_pred - y_train) ** 2)

# 测试集评估
Z_test = X_test @ W1.T + b1
A_test = tanh(Z_test)
y_test_pred = A_test @ W2.T + b2
test_mse = np.mean((y_test_pred - y_test) ** 2)
test_mae = np.mean(np.abs(y_test_pred - y_test))

print(f'训练集误差={train_mse:.2f}')
print(f'测试集误差={test_mse:.2f}')
print(f'测试集平均绝对误差={test_mae:.2f}')

#####################end###########################