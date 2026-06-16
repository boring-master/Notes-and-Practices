import numpy as np
# ------------------- 1. 数据读取 -------------------

data = np.genfromtxt('bp_data.csv', skip_header=1, delimiter=',', usecols=(0, 1))
x = data[:, 0:1]  # 保持二维 (m, 1)
y = data[:, 1:2]  # 保持二维 (m, 1)

# ----------------------------- 2. 数据归一化 -----------------------------
x_min, x_max = x.min(), x.max()
x_norm = (x - x_min) / (x_max - x_min) 


# ----------------------------- 3. 网络初始化 -----------------------------
input_size = 1
hidden_size = int(input('请录入隐藏层神经元个数='))   #从键盘录入隐藏层神经元个数
output_size = 1

np.random.seed(40)
W1 = np.random.randn(hidden_size, input_size)    # 
b1 = np.zeros(hidden_size)                  # 
W2 = np.random.randn(output_size, hidden_size)   # 
b2 = np.zeros(output_size)                  # 

# ----------------------------- 4. 激活函数 -----------------------------
def sigmoid(z):
    return 1/(1+np.exp(-z))

def sigmoid_derivative(z):
    return sigmoid(z)*(1 - sigmoid(z))

# ----------------------------- 5. 训练参数 -----------------------------
epochs = 1000
learning_rate = float(input('请录入学习率='))

m = len(x_norm)

# ----------------------------- 6. 批量梯度下降训练 -----------------------------
for epoch in range(epochs):
    # 批量前向传播（全部训练样本）
    Z1 = x_norm @ W1.T + b1                 # (m, hidden_size)
    A1 = sigmoid(Z1)                        # (m, hidden_size)
    y_pred = A1 @ W2.T + b2                 # (m, output_size)
                              
    # 反向传播（批量平均梯度）
    delta2 = (y_pred - y) / m               # (m, output_size)
    dW2 = delta2.T @ A1                     # (output_size, hidden_size)
    db2 = np.sum(delta2, axis=0)            # (output_size,)

    delta1 = (delta2 @ W2) * sigmoid_derivative(Z1)  # (m, hidden_size)
    dW1 = delta1.T @ x_norm                 # (hidden_size, input_size)
    db1 = np.sum(delta1, axis=0)            # (hidden_size)

    # 更新参数
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2
    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1


# ----------------------------- 7. 评估 -----------------------------
def predict(x_norm):
    Z1 = x_norm @ W1.T + b1
    A1 = sigmoid(Z1)
    y_pred = A1 @ W2.T + b2
    return y_pred

y_pred = predict(x_norm)
mse = np.mean((y_pred - y) ** 2)
print(f'MSE = {mse:.4f}')