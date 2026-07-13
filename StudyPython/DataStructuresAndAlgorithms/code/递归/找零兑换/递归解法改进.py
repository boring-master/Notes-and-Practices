import time
def recMC(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList:     # 最小规模
        knownResults[change] = 1    # 记录最优解
        return 1
    elif knownResults[change] > 0:  # 查表成功，直接使用最优解
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change - i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = numCoins
    return minCoins

a = time.time()
print(recMC([1, 5, 10, 25], 63, [0]*64))
print(f'{time.time()-a:.10f}')