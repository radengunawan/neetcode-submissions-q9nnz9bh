class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diffs = [gas[i] - cost[i] for i in range(n)]
        if sum(diffs) < 0:
            return -1
        
        start, tank = 0,0
        for i in range(n):
            tank += diffs[i]
            if tank <0:
                start = i + 1
                tank = 0
        
        return start
        