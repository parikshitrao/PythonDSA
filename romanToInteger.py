class Solution:
    def romanToInt(self, s: str) -> int:
        val_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, 'M': 1000}
        
        total = val_roman[s[-1]]  # Start from the last character
        
        for i in range(len(s) - 2, -1, -1):  # Loop from second-last to first
            curr = val_roman[s[i]]
            next_val = val_roman[s[i + 1]]
            
            if curr < next_val:
                total -= curr
                print("-", curr)
            else:
                total += curr
                print("+", curr)
        
        return total
