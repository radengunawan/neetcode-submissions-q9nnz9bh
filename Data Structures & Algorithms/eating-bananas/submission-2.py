class Solution:

    def ceil(self, p,k):
        result = p//k
        if (p%k > 0):
            result +=1
        return result

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        result = r

        while (l<= r):
            k = l + (r-l)//2

            hours = 0
            for pile in piles:
                hours += self.ceil (pile,k)

            if (hours <= h):
                result = min (result, k)
                r = k -1
            else:
                l = k +1
        
        return result


        