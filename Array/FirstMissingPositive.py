class FirstMissingPositive:
    def solution(self, nums):

        # l = len(nums)
        # hash_map = [0] * (l+1)


        # for i in nums:
        #     if 1 <= i <= l:
        #         hash_map[i]+=1

        # for i in range(1, l+1):
        #     if hash_map[i] == 0:
        #         return i

        # return l+1
        l = len(nums)

        for i in range(l):
            while 1 <= nums[i] <= l and nums[i] != nums[nums[i]-1]:
                c = nums[i] - 1

                nums[i], nums[c] = nums[c], nums[i]

        for i in range(l):
            if nums[i] != i+1:
                return i + 1

        return l+1
    
Solution = FirstMissingPositive()
print(Solution.solution([2,3,4]))

