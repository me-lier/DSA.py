class ValidAnagram():
    def solution(self, nums1, nums2):
        if len(nums1) != len(nums2):
            return False
        
        hash_map = {}

        for i in range(len(nums1)):
            hash_map[nums1[i]] = hash_map.get(nums1[i], 0) + 1
            hash_map[nums2[i]] = hash_map.get(nums2[i], 0) - 1
        
        for i in hash_map.values():
            if i != 0:
                return False

        return True

Solution = ValidAnagram()
print(Solution.solution([1,2,3,4], [4,3,2,2]))