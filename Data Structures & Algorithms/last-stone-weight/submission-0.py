class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            max_one = heapq.heappop(stones)
            max_two = heapq.heappop(stones)

            if max_two - max_one != 0:
                heapq.heappush(stones, max_one - max_two)
        stones.append(0)
        return -stones[0]