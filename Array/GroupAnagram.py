class GroupAnagram():
    def key(self, str):
        hash_map = [0] * 26

        for i in str:
            hash_map[ord(i) - ord('a')] +=1

        return tuple(hash_map)
    

    def solution(self, list1):
        
        hash_map = {}
        for i in list1:
            key = self.key(i)
            if key not in hash_map:
                hash_map[key] = []
            hash_map[key].append(i)

        return list(hash_map.values())
    
Solution = GroupAnagram()
print(Solution.solution(["eat","tea","tan","ate","nat","bat"]))            