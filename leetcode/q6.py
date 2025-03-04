class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        output = []
        for i in range(numRows):
            output.append([])
        for i in range(numRows):
            # 0,1,2,3,4...
            # construct each row
            for j in range(i, len(s)-1, numRows):
                output[i].append(s[j])
        print(output)

print(Solution().convert("PAYPALISHIRING", 3))
