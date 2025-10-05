class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Time Complexity: O(n), n is length of list
        Space Complexity: O(n), n is length of list
        Inputs:
        nums: List: this is used for checking each number
        k:int: This to track how far the next duplicate must be within
        Output:
        return a boolean if the condition is met or not
        """
        result_set = dict()
        for i in range(len(nums)):
            if nums[i] in result_set:
                if abs(i-(result_set[nums[i]]))<=k:
                    return True
                else:
                   result_set[nums[i]] = i
            else:  
                
                result_set[nums[i]] = i
        return False
        
