class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        m=min(nums)
        n=max(nums)
        res=[]
        for i in range(m+1,n):
            if i not in nums:
                res.append(i)
        return res
        