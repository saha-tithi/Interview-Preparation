#mathematic approach
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


#hashmap Approach 
#time complexity O(2n) space complexity O(n)
class Solution:
    def findMissingRepeatingNumbers(self, nums):
        n=len(nums)
        freq=[0]*(n+1)
        for num in nums:
            freq[num]+=1
        r=-1
        m=-1
        for i in range(1,n+1):
            if freq[i]==2:
                r=i
            elif freq[i]==0:
                m=i
        return [r,m]

