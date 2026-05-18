class Solution:
    def countBits(self, n: int) -> List[int]:

        def hammingWeight(m):
            res = 0

            while m:
                res += (m&1)
                m >>=1
            
            return res
        
        arr1 = [0]*(n+1)

        for i in range(n+1):
            arr1[i] = hammingWeight(i)
        
        return arr1
        