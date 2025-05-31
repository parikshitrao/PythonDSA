class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        no_of_str = len(strs)
        flag = 1
        j = 0

        while flag == 1:
            for i in range(no_of_str):
                if j >= len(strs[i]):
                    flag = 0
                    break
                elif strs[i][j] != strs[0][j]:  
                    flag = 0
                    break
            j += 1

        return strs[0][0:j-1] if j > 0 else ""  