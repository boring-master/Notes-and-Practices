import time
start = time.perf_counter() # 开始时间
'''
i = 0
while i < 100000000:
    i += 1
'''
for i in range(0,100000000):
    pass
end = time.perf_counter()   # 结束时间
print(end-start)



