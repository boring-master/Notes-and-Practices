import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"执行时间: {end - start:.4f}秒")
        return result
    return wrapper

@timing_decorator
def calculate_sum(a, b):
    return a + b

@timing_decorator
def calculate_product(a, b):
    return a * b

print(calculate_sum(10, 20))
print(calculate_product(5, 6))