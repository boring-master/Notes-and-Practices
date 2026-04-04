# def test_a():
#     num = 100
#     print(num)
# test_a()
# print(num) #报错：name 'num' is not defined

num = 200
def test_a():
    print(f'test_a:{num}')
def test_b():
    global num
    num = 500
    print(f'test_b:{num}')
test_a()
test_b()
print(num)

