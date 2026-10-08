class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = stoneSum // 2
        dp = {0}

        for stone in stones:
            new_dp = set(dp)
            for val in dp:
                if val + stone == target:
                    return stoneSum - 2 * target
                if val + stone < target:
                    new_dp.add(val + stone)
            dp = new_dp

        return stoneSum - 2 * max(dp)