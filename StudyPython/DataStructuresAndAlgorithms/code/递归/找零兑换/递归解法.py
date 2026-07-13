import time
def recMC(coinValueList, change):
    """
    :param coinValueList:硬币面值
    :param change:要找的零钱数
    :return:最少需要的硬币数
    """
    minCoins = change
    if change in coinValueList: # 最小规模
        return 1
    else:
        # 对小于零钱数的硬币面值进行遍历
        for i in [c for c in coinValueList if c <= change]:
            # 硬币数=1个i面值的硬币+减去i的零钱数所需找的硬币数
            numCoins = 1 + recMC(coinValueList, change - i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins

a = time.time()
print(recMC([1, 5, 10, 25],63))
print(f'{time.time()-a:.10f}')