class ContainsNearlyDuplicate():
    def solution(self, nums, k):
        seen = set()

        for i in range(len(nums)):
            if i > k:
                seen.remove(nums[i-k-1])
            if nums[i] in seen:
                return True
            seen.add(nums[i])

        return False
    

Solution = ContainsNearlyDuplicate()
print(Solution.solution([1,2,3,1,2,3], 3))