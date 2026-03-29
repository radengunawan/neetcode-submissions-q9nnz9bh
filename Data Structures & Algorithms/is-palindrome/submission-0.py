class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s2 = []
        for char in s:
            if char.isalnum():
                s2.append(char.lower())

        leftPtr, rightPtr = 0, len(s2) -1

        while (leftPtr < rightPtr):
            if s2[leftPtr] != s2 [rightPtr]:
                return False
            leftPtr +=1
            rightPtr -=1

        return True

            
        