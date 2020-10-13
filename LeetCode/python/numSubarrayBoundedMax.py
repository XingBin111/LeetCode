"""
题目: 返回子序列最大值在[L, R]中的个数
例:
Input:
A = [2, 1, 4, 3]
L = 2
R = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].


dp[i]作为以i为结尾的子序列最大值在[L, R]中的个数
1. A[i] < L and i > 0: dp[i] = dp[i-1]
2. A[i] > R: dp[i] = 0, 且记prev = i
3. L <= A[i] <= R: dp[i] = i - prev, 这是为了避免子序列中包含小于L的元素.
"""


class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        n = len(A)
        if n == 0:
            return 0
        res, dp = 0, 0
        prev = -1
        for i in range(n):
            if A[i] < L and i > 0:
                res += dp
            if A[i] > R:
                dp = 0
                prev = i
            if L <= A[i] <= R:
                dp = i - prev
                res += dp
        return res


if __name__ == "__main__":
    s = Solution()
    A = [73, 55, 36, 5, 55, 14, 9, 7, 72, 52]
    L = 32
    R = 69
    print(s.numSubarrayBoundedMax(A, L, R))
