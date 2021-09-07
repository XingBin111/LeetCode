import numpy as np
import bisect


class Solution:

    def maxWidthRamp(self, A):
        s = []
        res = 0
        for i, a in enumerate(A):
            if not s or A[s[-1]] > a:
                s.append(i)
        for j in range(len(A))[::-1]:
            while s and A[s[-1]] <= A[j]:
                res = max(res, j - s.pop())
        return res


if __name__ == "__main__":
    S = Solution()
    A = [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]

    print(S.maxWidthRamp(A))
