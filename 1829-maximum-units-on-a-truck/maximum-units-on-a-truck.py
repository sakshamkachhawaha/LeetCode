class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        total_units = 0
        for u, v in boxTypes:
            if u <= truckSize:
                truckSize -= u
                total_units += u * v
            else:
                total_units += truckSize * v
                break
        return total_units
