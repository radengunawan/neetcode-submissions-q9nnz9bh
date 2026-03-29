class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s or len(s)==1:
            return 1
        
        def expand(left, right):
            count = 0
            while (left >= 0 and right < len(s) and s[left]== s[right]):
                left -=1
                right +=1
                count +=1
            return count
        
        num_palin = 0
        for i in range (len(s)):
            num_palin += expand(i,i)
            num_palin += expand(i,i+1)

        return num_palin
        