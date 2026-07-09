class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        currGas = 0
        ans = 0
        for i in range(n):
            currGas += gas[i] - cost[i]
            if currGas < 0:
                currGas = 0
                ans = i + 1
        return ans