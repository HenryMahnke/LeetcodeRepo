class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #each row in matrix is in nondecreasing order 
        #first integer of every row is greater than last integer of previous row 
        #can just pretend the matrix is flattened
        width = len(matrix[0]) 
        height = len(matrix)
        l = 0
        r = width * height -1
        #if we were to consider a flattened array we would take numCols * 
        mid = (r + l) //2
        print(mid)

        while l <= r:
            mid = (r + l) //2
            # l+=1
            row = mid //width
            col = mid % width
            print(row,col)
            print(matrix[row][col])
            val = matrix[row][col]
            print(val)
            if val == target: 
                return True
            elif val < target: 
                l = mid +1 
            else: 
                r = mid-1
        return False

        
        