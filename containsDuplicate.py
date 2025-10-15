class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Time Complexity: O(n), where n is the length of list
        Space Complexity: O(n), where n is the length of list, because extra space of size N is allocated to the set in the worst case where the first and last numbers are duplicates or no duplicates exist
        Inputs:
        nums: List, a list of all values which are being expected.
        Output:
        returns a boolean if a duplicate exist
        """
        # Solution 1: Check if the length of set is matching the normal length but still creates the set and fills the values behind.
        # return len(set(nums))!=len(nums) #len of string vs len of set, as set doesnt include duplicates in it
        # Solution 2: Alternate method which manually appends to the set
        result_set = set()
        for i in nums:
            if i in result_set:
                return True
            result_set.add(i)
        return False
