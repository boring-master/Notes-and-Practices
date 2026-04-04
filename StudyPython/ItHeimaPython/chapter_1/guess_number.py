1# 目标数字
import random
secret_number = random.randint(1,10)
# 最多次数
guess_limit=3
# 已猜测次数
guess_number=0
while guess_number<guess_limit:
    guess=int(input('请输入0-9之间的数字：'))
    guess_number+=1
    if guess==secret_number:
        print('恭喜你，你赢了')
        break
print('游戏结束，正确数字为',secret_number)

