import math
import itertools
from sympy import symbols, Poly, gcd, div
from sympy.abc import x

def lagrange_interpolation(points):
    """
    拉格朗日插值法：根据给定点集构造插值多项式
    points: 列表，每个元素为元组 (x_i, y_i)
    返回：插值多项式的系数列表（从低次到高次）
    """
    n = len(points)
    poly = Poly(0, x)
    for i in range(n):
        xi, yi = points[i]
        # 构造拉格朗日基多项式 L_i(x)
        L_i = Poly(1, x)
        for j in range(n):
            if j != i:
                xj = points[j]
                L_i *= Poly(x - xj, x) / (xi - xj)
        poly += yi * L_i
    return poly.all_coeffs()

def get_divisors(n):
    """返回整数n的所有正负因数"""
    if n == 0:
        return 
    divisors = set()
    for i in range(1, int(math.sqrt(abs(n))) + 1):
        if abs(n) % i == 0:
            divisors.add(i)
            divisors.add(abs(n) // i)
    # 包含正负因数
    divisors = divisors.union({-d for d in divisors})
    return sorted(divisors)

def kronecker_irreducibility(f_coeffs, verbose=False):
    """
    克罗内克算法判定多项式在有理数域上的不可约性
    f_coeffs: 多项式系数列表，从低次到高次，如 [1, 0, 2] 表示 x^2 + 2
    返回: True（不可约） 或 False（可约）
    """
    # 构造SymPy多项式对象
    f = Poly(f_coeffs, x)
    n = f.degree()
    
    if n <= 1:
        return True  # 一次多项式在有理数域上不可约
    
    # 1. 选择插值点：从0, ±1, ±2, ..., ±(2n+1)中选n+1个使f(a)≠0的点
    candidates = []
    bound = 2 * n + 1
    for a in range(-bound, bound + 1):
        if f.eval(a) != 0:
            candidates.append(a)
            if len(candidates) == n + 1:
                break
    
    if len(candidates) < n + 1:
        raise ValueError(f"无法找到足够的插值点，仅找到{len(candidates)}个")
    
    if verbose:
        print(f"选择的插值点: {candidates}")
    
    # 2. 为每个点计算f(a_i)的所有因数
    divisors_list = []
    for a in candidates:
        fa = f.eval(a)
        divisors = get_divisors(fa)
        divisors_list.append(divisors)
        if verbose:
            print(f"f({a}) = {fa}, 因数: {divisors}")
    
    # 3. 枚举所有可能的(d0, d1, ..., dn)组合
    for d_vals in itertools.product(*divisors_list):
        # 构造插值点集 (a_i, d_i)
        points = list(zip(candidates, d_vals))
        
        # 拉格朗日插值得到h_d(x)
        try:
            h_coeffs = lagrange_interpolation(points)
            h = Poly(h_coeffs, x)
            
            # 跳过常数多项式
            if h.degree() == 0:
                continue
            
            # 4. 检查h_d(x)是否整除f(x)
            _, remainder = div(f, h)
            
            if remainder == 0 and h.degree() > 0 and h.degree() < n:
                if verbose:
                    print(f"找到真因子: h(x) = {h.as_expr()}")
                    print(f"因式分解: f(x) = ({h.as_expr()}) * ({div(f, h)[0].as_expr()})")
                return False  # 可约
                
        except Exception as e:
            # 忽略插值或除法中的数值误差
            continue
    
    return True  # 不可约

def test_polynomials():
    """测试函数：验证几个常见多项式的不可约性"""
    test_cases = [
        ([1, 0, -1], "x^2 - 1 (可约: (x-1)(x+1)"),
        ([1, 1, 1], "x^2 + x + 1 (在Q上不可约)"),
        ([1, 0, 0, -1], "x^3 - 1 (可约: (x-1)(x^2+x+1)"),
        ([1, 0, 2], "x^2 + 2 (在Q上不可约)"),
        ([1, 0, -2], "x^2 - 2 (在Q上不可约)"),
        ([1, 2, 3, 2, 1], "x^4 + 2x^3 + 3x^2 + 2x + 1 (可约: (x^2+x+1)^2)")
    ]
    
    for coeffs, desc in test_cases:
        is_irred = kronecker_irreducibility(coeffs, verbose=False)
        result = "不可约" if is_irred else "可约"
        print(f"{desc} -> {result}")

if __name__ == "__main__":
    # 示例用法
    print("克罗内克不可约性判定算法")
    print("=" * 50)
    
    # 测试示例多项式
    test_polynomials()
    
    print("\n" + "=" * 50)
    print("自定义多项式测试:")
    
    # 自定义测试：x^2 - 2
    custom_poly = [1, 0, -2]  # 代表 x^2 - 2
    print(f"测试多项式: x^2 - 2")
    result = kronecker_irreducibility(custom_poly, verbose=True)
    print(f"结果: {'不可约' if result else '可约'}")
    
    # 自定义测试：x^2 - 1 (可约)
    custom_poly2 = [1, 0, -1]  # 代表 x^2 - 1
    print(f"\n测试多项式: x^2 - 1")
    result2 = kronecker_irreducibility(custom_poly2, verbose=True)
    print(f"结果: {'不可约' if result2 else '可约'}")
