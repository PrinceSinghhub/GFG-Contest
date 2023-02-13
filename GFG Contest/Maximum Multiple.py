from typing import List


class Solution:
    def maximumMultiple(self, N: int, A: List[int]) -> int:
        A.sort()
        count = 0
        for i in A:
            if i < 0:
                count += 1

        if count * 2 == N:
            A = A[0:N // 2] + A[N // 2::][::-1]

        Max = -(10 ** 18)
        for i in range(N):
            Max = max(Max, (A[i] * A[N - i - 1]))

        return Max
