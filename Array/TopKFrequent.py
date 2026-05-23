import heapq
class TopKFrequent():
    def solution(self, nums, k):
        hash_map = {}

        for i in nums:
            hash_map[i] = hash_map.get(i, 0) + 1

        # pq = []
        # for i, j in hash_map.items():
        #     heapq.heappush(pq, (-j,i))

        # ans = []
        # for i in range(k):
        #     ans.append(heapq.heappop(pq)[1])

        # return ans

        #bucket Sort

        freq = [[] for _ in range(len(nums) + 1)]

        for i , j in hash_map.items():
            freq[j].append(i)


        ans = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                ans.append(num)

                if len(ans) == k:
                    return ans
    
Solution = TopKFrequent()
print(Solution.solution([1,2,1,1,4,5,6,6,5,5,5], 3))