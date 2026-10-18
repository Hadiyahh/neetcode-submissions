class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        # right = n
        # left = 0
        def find_middle(left,right,c): # up down, i feel like i could even keep the binary search methid but have the variables change
            # left top of the row
            # right is bottom of the row 
            # since we are searching the row c will stay constant
            while left <= right:
                mid = left + (right - left) // 2 
                if matrix[mid][c] <= target <= matrix[mid][n-1]: # is the element in this row
                    return mid # the row we will traverse
                elif matrix[mid][n-1] < target:
                    left = mid + 1
                elif matrix[mid][c] > target:
                    right = mid - 1
                else:
                    return False
        row = find_middle(0,m-1,0) # returns the row we should traverse
        print(row)        

        if row is not False and row is not None:
            right = n -1
            left = 0
            for column in range(n):
                while left <= right:
                    mid = left + (right - left) // 2
                    print("mid2:", mid)
                    if matrix[row][mid] == target:
                        return True
                    elif matrix[row][mid] < target:
                        left = mid + 1
                    else: # matrix[row][mid] > target:
                        right = mid - 1
        return False
            