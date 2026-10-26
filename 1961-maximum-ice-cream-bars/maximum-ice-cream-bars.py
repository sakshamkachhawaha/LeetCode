class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        ice = 0
        for i in range(len(costs)):
            if costs[i]<=coins:
                ice+=1
                coins-=costs[i]
        return ice