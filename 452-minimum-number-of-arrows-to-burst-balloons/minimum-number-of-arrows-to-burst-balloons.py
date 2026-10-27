class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort()
        start = points[0][0]
        end = points[0][1]
        cnt = 1
        for i in range(1,len(points)):
            if points[i][0]<=end:
                start = points[i][0]
                end = min(end,points[i][1])
            else:
                cnt+=1
                start = points[i][0]
                end = points[i][1]
                
        return cnt 