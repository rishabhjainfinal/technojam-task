# Given an integer n and an integer start.
# Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.
# Return the bitwise XOR of all elements of nums.

class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums= [0 for i in range(n)]
        for i in range(n):
            nums[i] = start + 2*i

        return self.bitwise_XOR_result(nums)

    def bitwise_XOR_result(self,array):
        if len(array) : return array.pop() ^ self.bitwise_XOR_result(array)
        else : return 0
a =  Solution()
print(a.xorOperation(10,5))