class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        final = []
        hm = {}
        # need to progress both counters by 2 if progress
        # always need to pick either  0th or 1st to progress
        # check which ones bigger
        # essentially need to pick a largest eventually, otherwise miss out
        # maximum this range is +1 extra, aka 2 look ahead instead of 1 look ahead
        for i in range(1, len(nums), 2):
            choice = [nums[i-1], nums[i]]
            larger = max(nums[i-1], nums[i])
            if choice[0] > choice[1]:
                # go down path i-1
                # need to swap?
                final.append(larger)
            else:
                # go down path i
                final.append(larger)


print(Solution().rob([2,7,9,3,1]))
print(Solution().rob([2,1,1,2]))
