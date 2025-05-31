class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count, max_count = 0,0
        seen={}
        i=0
        while i < len(s):
            if s[i] in seen:
                max_count = max_count if max_count > count else count
                print("max_count")
                count = 0
                i = seen[s[i]] + 1
                seen.clear()
            else:
                seen[s[i]]=i
                count += 1
                i+=1
                # print(s[i])

        return max(max_count,count)