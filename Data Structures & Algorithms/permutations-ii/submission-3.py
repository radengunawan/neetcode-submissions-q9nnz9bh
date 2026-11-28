class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        count = {n: 0 for n in nums}
        for num in nums:
            count[num] += 1

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for num in count:
                if count[num] > 0:
                    perm.append(num)
                    count[num] -= 1
                    dfs()
                    count[num] += 1
                    perm.pop()

        dfs()
        return res