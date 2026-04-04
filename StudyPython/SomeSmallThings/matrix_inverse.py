import numpy as np

def compute_matrix_inverse(matrix_array):
    """
    计算给定NumPy数组（矩阵）的逆矩阵。

    参数:
        matrix_array (np.ndarray): 一个二维NumPy数组，代表待求逆的矩阵。

    返回:
        np.ndarray 或 str: 如果矩阵可逆，返回其逆矩阵；否则返回错误信息字符串。
    """
    # 1. 检查输入是否为二维数组（即矩阵）
    if matrix_array.ndim != 2:
        return "错误：输入必须是一个二维数组（矩阵）。"

    # 2. 检查矩阵是否为方阵（行数等于列数）
    rows, cols = matrix_array.shape
    if rows != cols:
        return f"错误：矩阵不是方阵（形状为 {matrix_array.shape}），方阵才可能可逆[1](@ref)。"

    # 3. 检查矩阵是否可逆（行列式是否非零）
    # 注意：对于浮点数，由于精度问题，行列式绝对值极小也可能视为奇异。
    det = np.linalg.det(matrix_array)
    if np.abs(det) < 1e-10:  # 设置一个小的容差阈值
        return "错误：矩阵行列式（近似）为零，该矩阵是奇异矩阵，不可逆[1](@ref)[5](@ref)。"

    # 4. 计算逆矩阵
    try:
        inverse_matrix = np.linalg.inv(matrix_array)
        return inverse_matrix
    except np.linalg.LinAlgError:
        # 尽管已检查行列式，但某些病态矩阵仍可能引发异常
        return "错误：计算逆矩阵时发生数值错误，矩阵可能接近奇异或不可逆[2](@ref)[5](@ref)。"


# ===== 示例使用 =====
if __name__ == "__main__":
    # 示例1：可逆的2x2矩阵
    print("示例1：可逆的2x2矩阵")
    A = np.array([[1, 2],
                  [3, 4]])
    print(f"原矩阵 A:\n{A}")
    result = compute_matrix_inverse(A)
    if isinstance(result, np.ndarray):
        print(f"逆矩阵 A_inv:\n{result}")
        # 验证：A * A_inv 应近似于单位矩阵
        verification = np.dot(A, result)
        print(f"验证 A * A_inv (应接近单位矩阵):\n{verification}")
    else:
        print(result)

    print("\n" + "="*50 + "\n")

    # 示例2：不可逆（奇异）矩阵
    print("示例2：奇异矩阵（不可逆）")
    B = np.array([[1, 2],
                  [2, 4]])  # 第二行是第一行的两倍，行列式为0
    print(f"原矩阵 B:\n{B}")
    print(compute_matrix_inverse(B))

    print("\n" + "="*50 + "\n")

    # 示例3：3x3矩阵
    print("示例3：3x3矩阵")
    C = np.array([[4, 7, 2],
                  [3, 6, 1],
                  [2, 5, 8]])
    print(f"原矩阵 C:\n{C}")
    result = compute_matrix_inverse(C)
    if isinstance(result, np.ndarray):
        print(f"逆矩阵 C_inv:\n{result}")
    else:
        print(result)
