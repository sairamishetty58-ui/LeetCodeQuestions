class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            #  empty string
            output = ""
            # edge cases if the list is empty or 1 word
            if len(strs) ==1:
                return strs[0]
            if len(strs)==0:
                return output
            # finding the min length of the list
            min_length = 1000
            for i in strs:
                if len(i)<min_length:
                    min_length = len(i)
            # loop throught min length to check each char upto min length
            for i in range(min_length):
                # get first word ith positin
                first_char = strs[0][i]
                # compare with the rest
                for word in strs[1:]:
                    # if doesnt match return current out[ut]
                    if word[i] != first_char:
                        return output
                # if all words match append output 
                output+=first_char
            return output
