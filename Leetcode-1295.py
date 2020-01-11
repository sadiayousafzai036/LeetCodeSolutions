class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        eventotal = 0
        n = len(nums)
        for i in range(0, n):
            if len(str(nums[i]))%2==0:
                eventotal += 1
        return eventotal


t1 = Solution()
print(t1.findNumbers([437,315,322,431,686,264,442]))