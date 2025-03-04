class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if str(x)[0] == "-":
            # negative int case
            a = -int(str(x)[1:][::-1])
            if abs(a) >= 2**31:
                return 0
            return a
        else:
            a = int(str(x)[::-1])
            if a >= 2**31:
                return 0
            return a
