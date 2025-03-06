
import heapq as hq

class Point:
    x = 0
    y = 0

class Solution:
    @staticmethod 
    def main():
        minHeap = [5, 6 ,2 ,1]
        hq.heapify(minHeap)
        hq.heappush(minHeap, 3)
        print(minHeap)

        while len(minHeap):
            val = hq.heappop(minHeap)
            print(val)
        print("Done!")

 

 
Solution.main()