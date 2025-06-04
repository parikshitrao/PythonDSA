class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        seen = set()
        for i in ransomNote:
            flag = 0
            for j in range(len(magazine)):
                if magazine[j] == i and j not in seen :
                    flag = 1
                    seen.add(j)
                    break
            if flag == 0:
                return False
        return True