class ContainsDuplicate():
    def solution(self, nums):
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)

        return False
    

Solution = ContainsDuplicate()
print(Solution.solution([1,2,3,4]))