class Solution:
    def solve(self, N, K, A):

        mydic = {}

        for i in A:
            if i not in mydic:
                mydic[i] = 1
            else:
                mydic[i] += 1

        print(mydic)

        for i in range(2 * N + 1):
            if i not in mydic:
                K -= 1
            if K == 0:
                return i
        return -1
    