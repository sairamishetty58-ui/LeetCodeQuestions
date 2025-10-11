class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        remain = len(nums)
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                remain-=1
                i-=1
            i+=1
        return remain
        
