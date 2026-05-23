class IsAlienSorted():
    def solution(self, words, order):
        hash_map = {}
        for i , j in enumerate(order):
            hash_map[j] = i

        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return False

                if words[i][j] == words[i+1][j]:
                    continue

                if hash_map[words[i][j]] > hash_map[words[i+1][j]]:
                    return False

                break

        return True
    
Solution = IsAlienSorted()
print(Solution.solution(["word","world","row"], "worldabcefghijkmnpqstuvxyz"))