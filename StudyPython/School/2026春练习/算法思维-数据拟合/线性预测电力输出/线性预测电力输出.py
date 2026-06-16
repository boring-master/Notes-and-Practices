#请读取数据文件"Folds5x2_pp.csv",编写代码对输出电力进行预测
import numpy as np   
seed=eval(input('请输入随机数种子:'))
np.random.seed(seed)
w=np.random.randn(5) #初始化各列的权重
lr=eval(input('请输入学习率:'))
rounds=eval(input('请输入数据集迭代轮数:'))
data=np.genfromtxt('Folds5x2_pp.csv',skip_header = 1,delimiter=',',usecols=(1,2,3,4,5))
np.random.shuffle(data)  #随机打乱examples
data=data[0:2000,:]
X=data[:,0:-1] 
X=(X-X.min(axis=0))/(X.max(axis=0)-X.min(axis=0)) #归一化
X_b=np.concatenate((np.ones((len(X), 1)), X), axis=1)
y=data[:,-1]

#训练集测试集划分
testRate=0.2 #测试集的占比
X_test=X_b[0:int(len(X)*testRate)] #按比例划分训练集和测试集
y_test=y[0:int(len(X)*testRate)]
X_train=X_b[int(len(X)*testRate):]
y_train=y[int(len(X)*testRate):]
#####################begin###############################
m = len(X_train)

# 批量梯度下降迭代拟合
for i in range(rounds):
    # 计算预测值
    y_pred = X_train.dot(w)
    # 计算误差
    error = y_pred - y_train
    # 计算梯度
    gradient = (X_train.T.dot(error)) / m
    # 更新权重
    w = w - lr * gradient

# 计算训练集误差(mse)
train_pred = X_train.dot(w)
train_mse = np.mean((train_pred - y_train) ** 2)

# 计算测试集误差(mse)
test_pred = X_test.dot(w)
test_mse = np.mean((test_pred - y_test) ** 2)

# 计算测试集平均绝对误差(mae)
test_mae = np.mean(np.abs(test_pred - y_test))

# 保留2位小数输出结果
print(f'训练集误差mse={train_mse:.2f}')
print(f'测试集误差mse={test_mse:.2f}')
print(f'测试集mae={test_mae:.2f}')
###################end######################