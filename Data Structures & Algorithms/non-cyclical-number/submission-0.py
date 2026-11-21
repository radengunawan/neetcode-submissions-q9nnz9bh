class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquares(n)
        power = lam = 1

        while slow != fast:
            if power == lam:
                slow = fast
                power *= 2
                lam = 0
            fast = self.sumOfSquares(fast)
            lam += 1
        return True if fast == 1 else False

    def sumOfSquares(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output