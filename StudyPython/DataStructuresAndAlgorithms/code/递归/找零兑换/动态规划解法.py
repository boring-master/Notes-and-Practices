import time
def dpMakeChange(coinValueList,change,minCoins):
    # 从1分开始到change逐个计算最少硬币数
    for cents in range(change+1):
        # 1. 初始化一个最大值
        coinCount = cents
        # 2. 减去每个硬币，向后查最少硬币数，同时记录总的最少数
        for j in [c for c in coinValueList if c <= cents]:
            # 如果零钱数减去j所需找的硬币数+1个j面值的硬币<最大值
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j]+1
        # 3. 得到当前最少硬币数，记录到表中
        minCoins[cents] = coinCount
    return minCoins[change]

a = time.time()
print(dpMakeChange([1, 5, 10, 21, 25],63,[0]*64))
print(f'{time.time()-a:.10f}')