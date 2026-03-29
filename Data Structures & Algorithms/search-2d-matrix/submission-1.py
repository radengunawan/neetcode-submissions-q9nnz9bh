class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #binary search on a pseudo "1D" array

        ROWS, COLS = len(matrix), len(matrix[0])

        #1D array approach
        left, right = 0, ROWS*COLS -1

        while left <= right:
            mid = left + (right - left)//2 
            # need 2D info from pseudo 1D array
            row_mid, col_mid = mid//COLS, mid%COLS

            if(target > matrix[row_mid][col_mid]):
                left = mid + 1
            elif (target < matrix[row_mid][col_mid]):
                right = mid -1
            else:
                return True

        return False
    
        '''
        #brute force approach (traditional, O(MxN))
        m = len(matrix)

        for i in range (m):
            if (target in matrix[i]):
                return True

        return False
        '''
        