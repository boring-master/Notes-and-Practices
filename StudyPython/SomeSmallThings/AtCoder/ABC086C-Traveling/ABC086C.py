import sys
iterator=iter(sys.stdin.read().split())
N=int(next(iterator))
prev_t,prev_x,prev_y=0,0,0
for i in range(N):
    t=int(next(iterator))
    x=int(next(iterator))
    y=int(next(iterator))
    dt=t-prev_t
    dist=abs(x-prev_x)+abs(y-prev_y)
    if dist>dt or (dt-dist)%2!=0:
        print('No')
        break
    prev_t,prev_x,prev_y=t,x,y
else:
    print('Yes')