class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = [[]]

        for num in nums:
            new_subset = []
            for subset in res:
                new_subset.append(subset + [num])
            
            res += new_subset
        
        return res
