import time
gift_box = set()
while True:
    print('# 若不再添加请输入0')
    in_put = input('你要添加的奖品是：')
    if in_put == '0':
        if gift_box:
            result = gift_box.pop()
            print('开始抽奖')
            time.sleep(0.5)
            print(f'你抽到了{result}')
            break
        else:
            print('-请至少添加一个奖品-')

    else:
        gift_box.add(in_put)
