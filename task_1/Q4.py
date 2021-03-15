# You are given two strings word1 and word2. 
# Merge the strings by adding letters in alternating order, 
# starting with word1. If a string is longer than the other,
# append the additional letters onto the end of the merged string.
# Return the merged string.





class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        return_str = ""
        if len(word1) == len(word2):
            for a,b in zip(word1,word2):
                return_str += a+b
        else :
            max_len = min(len(word1),len(word2))
            for a,b in zip(word1[0:max_len],word2[0 : max_len]):
                return_str += a+b
            return_str += word1[max_len:] + word2[max_len:]

        return return_str

a =  Solution()
word1 = "ab"
word2 = "pqrs"
print(a.mergeAlternately(word1,word2))