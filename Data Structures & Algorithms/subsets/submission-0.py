class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        current, final = [], []

        def dfs(start):
            final.append(current.copy())

            for i in range (start, len(nums)):
                current.append(nums[i])
                dfs (i+1)
                current.pop()

        dfs(0)
        return final
        