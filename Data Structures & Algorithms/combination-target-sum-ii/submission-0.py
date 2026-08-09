class Solution:
    def combinationSum2(self, nums, target):
        self.res = []
        self.count = defaultdict(int)
        cur = []
        A = []

        for num in nums:
            if self.count[num] == 0:
                A.append(num)
            self.count[num] += 1
        self.backtrack(A, target, cur, 0)
        return self.res

    def backtrack(self, nums, target, cur, i):
        if target == 0:
            self.res.append(cur.copy())
            return
        if target < 0 or i >= len(nums):
            return

        if self.count[nums[i]] > 0:
            cur.append(nums[i])
            self.count[nums[i]] -= 1
            self.backtrack(nums, target - nums[i], cur, i)
            self.count[nums[i]] += 1
            cur.pop()

        self.backtrack(nums, target, cur, i + 1)