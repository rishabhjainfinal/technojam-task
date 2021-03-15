# Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
# A lucky number is an element of the matrix such that 
# it is the minimum element in its row and maximum in its column.

class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        shape = (len(matrix),len(matrix[0]))
        luckyNumbers = []
        for row in range(shape[0]):
            for col in range(shape[1]):
                # print(matrix[row][col],row,col)
                # min in row and max in col
                if matrix[row][col] == min(matrix[row]) and matrix[row][col] == max([ele[col] for ele in matrix]):
                    luckyNumbers.append(matrix[row][col])

        return luckyNumbers

a =  Solution()
matrix = [[3,7,8],[9,11,13],[15,16,17]]
matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
print(a.luckyNumbers(matrix))