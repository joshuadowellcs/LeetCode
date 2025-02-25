#Given an integer numRows, return the first numRows of Pascal's triangle.

#In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

#Example 1:

#Input: numRows = 5
#Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#Example 2:

#Input: numRows = 1
#Output: [[1]]

#Starting code 
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return [0]
        if numsRows == 1:
            return [1]
        
        prevRows = self.generate(numRows - 1)
        newRow = [1] * numRows

        for i in range(1, numRows - 1):
            newRow[i] = prevRows[-1][i - 1] + prevRows[-1][i]
        
        prevRows.append(newRow)
        return prevRows
        
 