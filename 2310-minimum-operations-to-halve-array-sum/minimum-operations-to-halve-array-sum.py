class Solution:
    def halveArray(self, nums: list[int]) -> int:
        import heapq
        heap = [-x for x in nums]
        heapq.heapify(heap)

        total = sum(nums)
        heap_sum = total
        cnt = 0
        while abs(heap_sum)>total/2:
            cnt+=1
            top = -heapq.heappop(heap)
            heap_sum -= top/2
            heapq.heappush(heap,-top/2)
        return cnt