class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        hm = {}
        for i in range(len(s)):
            if s[i] not in hm:
                hm[s[i]] = [i];
            else:
                hm[s[i]].append(i)
        # delete all 1 instances as they cant be palindromes
        longest = s[0];
        for i in range(len(s)):
            for pos in hm[s[i]]:
                if pos <= i:
                    possible = s[pos:i+1]
                    # print(f"pos {possible} cut: {i} {pos} ")
                    if possible == possible[::-1]:
                        if(len(possible)>len(longest)):
                            longest = possible
                            break
        return longest
print(Solution().longestPalindrome("abc"))
print(Solution().longestPalindrome("abcba"))
