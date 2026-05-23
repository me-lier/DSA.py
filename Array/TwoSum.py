class TwoSum():
    def solution(self, nums, target):
        hash_map = {}
        for i in range(len(nums)):
            if (target - nums[i]) in hash_map:
                return [i, hash_map[target - nums[i]]]
            hash_map[nums[i]] = i

        return [-1, -1]
    

Solution = TwoSum()

print(Solution.solution([1,2,3,4,5,6], 9))