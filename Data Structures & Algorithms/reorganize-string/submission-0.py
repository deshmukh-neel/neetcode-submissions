class Solution:
    def reorganizeString(self, s: str) -> str:
        from collections import Counter
        import heapq

        freq = Counter(s)
        
        maxHeap = [[-count, character] for character, count in freq.items()]
        heapq.heapify(maxHeap)
        res = ""

        prev = None

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            count, char = heapq.heappop(maxHeap)
            res += char
            count += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if count != 0:
               prev = [count, char]
        return res
            
        

