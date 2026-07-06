import timeit
popzero = timeit.Timer('x.pop(0)', 'from __main__ import x')
popend = timeit.Timer('x.pop()', 'from __main__ import x')
print('pop(0)    pop()')
for i in range(1000000,100000001,1000000):
    x = list(range(i))
    pt = popend.timeit(number=1000)
    pz = popzero.timeit(number=1000)
    print(f'{pz:7.5f}   {pt:7.5f}')