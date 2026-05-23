class ProductOfArrayExceptSelf():
    def solution(self, nums):
        l = len(nums)
        ans = [1] * l
        prefix = 1

        for i in range(l):
            ans[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(l-1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]

        return ans
    
Solution = ProductOfArrayExceptSelf()
print(Solution.solution([1,2,3,4]))

