class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        if len(num1) < len(num2):
            return self.multiply(num2, num1)

        res, zero = "", 0
        for i in range(len(num2) - 1, -1, -1):
            cur = self.mul(num1, num2[i], zero)
            res = self.add(res, cur)
            zero += 1

        return res

    def mul(self, s: str, d: str, zero: int) -> str:
        i, carry = len(s) - 1, 0
        d = int(d)
        cur = []

        while i >= 0 or carry:
            n = int(s[i]) if i >= 0 else 0
            prod = n * d + carry
            cur.append(str(prod % 10))
            carry = prod // 10
            i -= 1

        return ''.join(cur[::-1]) + '0' * zero

    def add(self, num1: str, num2: str) -> str:
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        res = []

        while i >= 0 or j >= 0 or carry:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            total = n1 + n2 + carry
            res.append(str(total % 10))
            carry = total // 10
            i -= 1
            j -= 1

        return ''.join(res[::-1])