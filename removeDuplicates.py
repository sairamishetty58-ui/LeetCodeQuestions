class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      
        i,j = 0,1
        duplicate_count = 0
        len_nums = len(nums)
        while j<len(nums):
            if nums[i] == nums[j]:
                nums.pop(j)
                duplicate_count +=1
                j-=1
                i-=1
            
            
            i+=1
            j+=1
        return len_nums-duplicate_count
