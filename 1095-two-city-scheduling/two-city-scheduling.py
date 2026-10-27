class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:

        def f(city):
            return city[0] - city[1]

        costs.sort(key = f )
        a = 0
        for i in range(len(costs)):
            if i<len(costs)//2:
                a+=costs[i][0]
            else:
                a+=costs[i][1]
        return a