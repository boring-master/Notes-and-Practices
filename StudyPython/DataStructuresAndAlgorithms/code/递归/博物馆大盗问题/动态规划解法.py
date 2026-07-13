tr = [None,
      {'w': 2, 'v': 3},
      {'w': 3, 'v': 4},
      {'w': 4, 'v': 8},
      {'w': 5, 'v': 8},
      {'w': 9, 'v': 10}]
max_w = 20
# 初始化二维表格m[(i, w)]
# 前i个宝物中，最大重量w的组合所得到的最大价值
m = {(i, w): 0 for i in range(len(tr)) for w in range(max_w + 1)}

for i in range(1, len(tr)):
    for w in range(1, max_w + 1):
        if tr[i]['w'] > w:# 如果第i个宝物的重量大于当前的最大负重w
            m[(i, w)] = m[(i-1, w)] # 不装第i个宝物
        else:           # 不装第i个宝物与装第i个宝物两种情况下的最大价值
            m[(i, w)] = max(m[(i-1, w)], m[(i-1, w-tr[i]['w'])] + tr[i]['v'])
print(m[(len(tr)-1, max_w)])