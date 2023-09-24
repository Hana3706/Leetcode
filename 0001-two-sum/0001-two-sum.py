class Solution(object):
    def twoSum(self, nums, target):
        answer=[]
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            start=i+1
            for j in range(start,len(nums)):
                if nums[i]+nums[j]==target:
                    answer=[i,j]
        return answer





        