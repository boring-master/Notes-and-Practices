def say_hello():
    print('Hello...')
result = say_hello()
print(result)
print(type(result))

def say_hello():
    print('Hello...')
    return None
result = say_hello()
print(result)

def check_age(age):
    if age > 18:
        return 'SUCCESS'
    else:
        return None
result = check_age(16)
if not result:
    print('未成年，不可以进入')

