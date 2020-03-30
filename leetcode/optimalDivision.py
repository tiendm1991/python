from  datetime import datetime


class Solution:
    def optimalDivision(self, nums) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        if n <= 2:
            return str(nums[0]) + '/' + str(nums[1])
        s = '/'.join([str(nums[i]) for i in range(1, n)])
        return str(nums[0]) + '/({})'.format(s)


s = Solution()
startTime = datetime.now()
print(s.optimalDivision([3,2]))
print(datetime.now() - startTime)