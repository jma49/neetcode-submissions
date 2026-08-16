class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        fuel = 0
        start = 0

        if sum(gas) < sum(cost):
            return -1
        
        for i in range(len(gas)):
            if fuel + gas[i] - cost[i] < 0:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return start