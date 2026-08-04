class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        check=n//3
        freq={}
        ans=[]
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for key,value in freq.items():
            if value>check:
                ans.append(key)
        return ans

        
       