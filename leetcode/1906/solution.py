from bisect import bisect_left

class Solution:
    def minDifference(self, nums, Q):
        inf = float('inf')
        idx = {}
        for i, v in nums:
            if v not in idx:
                idx[v] = []
            idx[v].append(i)

        def check(a, l, r):
            i = bisect_left(a, r)
            return i != len(a) and a[i] <= r

        def find(l, r):
            ret = inf
            for i in range(1, 101):
                if check(idx[i], l, r):
                    if prev != 0:
                        ret = min(ret, i - prev)
                    prev = i
            return -1 if ret == float('inf') else ret

        return [find(l, r) for l, r in Q]

nums = [4,5,2,2,7,10]; queries = [[2,3],[0,2],[0,5],[3,5]]
sol = Solution().minDifference
print(sol(nums, queries))
