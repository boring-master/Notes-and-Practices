class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return (n % 2 + 1) * n
        # return n if n % 2 == 0 else n * 2
        # return n << (n & 1)