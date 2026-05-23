class RomanToIntegers():
    def solution(self, s):

        hash_map = {
            'I' : 1,
            # 'IV' : 4,
            'V' : 5,
            # 'IX' : 9,
            'X' : 10,
            # 'XL' : 40,
            'L' : 50,
            # 'XC' : 90,
            'C' : 100,
            # 'CD' : 400,
            'D' : 500,
            # 'CM' : 900,
            'M' : 1000
        }
        # j = 0
        # for i in range(len(s) - 1):
        #     if j != 0:
        #         j-=1
        #         continue
        #     key = ''.join(j for j in s[i:i+2])
        #     if key in hash_map.keys():

        #         ans += hash_map.get(s[i:i+2])
        #         j = 1
        #         continue
        #     ans += hash_map[s[i]]
        # if j != 0:
        #     return ans
        # ans += hash_map[s[-1]]

        # return ans
        ans = 0
        for i in range(len(s) -1):
            if hash_map[s[i]] < hash_map[s[i+1]]:
                ans -= hash_map[s[i]]
            else:
                ans += hash_map[s[i]]
        

        return ans + hash_map[s[-1]]
    
Solution = RomanToIntegers()
print(Solution.solution('XCDM'))