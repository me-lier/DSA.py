class LongestConsecutive():
    def solution(self, nums):
        if not nums:
            return 0
        # if not nums:
        #     return 0
        # nums = sorted(nums)

        # m = 1
        # c = 1
        
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i+1]: 
        #         continue
        #     if nums[i] + 1 == nums[i+1]:
        #         c += 1
        #     else:
        #         c = 1

        #     m = max(m, c)
        
        # return m
        hash_set = set(nums)

        m = 1
        for i in hash_set:
             if i - 1 not in hash_set:
                c = 1

                while i+c in hash_set:
                    c+=1
                m = max(m, c)
        
        return m