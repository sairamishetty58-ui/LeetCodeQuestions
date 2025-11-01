class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        
        PseudoCode
        Create an dictionary, when the list is iterated through the difference is the calculated and set to the index, if the difference exists in the list, the difference index and the current index are returned
        Time Complexity: O(N): Loops through all the numbers of the list nums, N is the length of the list.
        Space Complexity: O(N): Worst case is when the first and last number add to the target, all the prior elements will be stored in the dictonary.
        Inputs:
        nums: List, contains all the numbers where one solution occurs
        target: int, what the sum of the two numbers in nums must add upto
        Output:
        List[int]: returns the integer of the index which sum up to the target
        """
        # Creates an empty dictionary to store all the difference between target and nums[i] values and their index 
        res_dict = {}
        # Loops through the list
        for i in range(len(nums)):
            diff = target - nums[i]
            # if result in dictionary, return the index of the first value and current i pointer
            if diff in res_dict:
                return [res_dict[diff], i]   
            # if not in dict, add to the dictionary
            res_dict[nums[i]] = i
