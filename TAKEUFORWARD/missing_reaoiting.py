class Solution:
    def findMissingRepeatingNumbers(self, nums):
        n=len(nums)
        actual_sum=sum(nums)
        expected_sum=n*(n+1)//2
        expected_sq_sum=n*(n+1)*(2*n+1)//6
        actual_sq_sum=sum(num*num for num in nums)
        diff=actual_sum-expected_sum
        sq_diff=actual_sq_sum-expected_sq_sum
        sum_xy=sq_diff//diff
        x=(diff+sum_xy)//2
        y=sum_xy-x
        return[x,y]

