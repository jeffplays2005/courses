class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        hm = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        stack = []
        total = 0
        for i in range(len(s)-1, -1, -1):
            char = s[i]
            if not stack:
                stack.append(hm[char])
            else:
                last = stack[-1]
                current = hm[char]
                # everything should only get bigger
                if current < last:
                    stack[-1]-=current
                else:
                    stack.append(current)
        return sum(stack)

print(Solution().romanToInt("III"))
print(Solution().romanToInt("VIII"))
print(Solution().romanToInt("MCMXCIV"))
