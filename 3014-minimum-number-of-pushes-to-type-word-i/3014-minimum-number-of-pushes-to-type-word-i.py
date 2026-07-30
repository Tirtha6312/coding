class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)

        max_heap = []

        for f in freq.values():
            heapq.heappush(max_heap, -f) 

        ans = 0
        index = 0

        while max_heap:

            frequency = -heapq.heappop(max_heap)

            presses = index // 8 + 1

            ans += frequency * presses

            index += 1

        return ans
