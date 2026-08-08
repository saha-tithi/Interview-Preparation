class Solution:
    def searchMatrix(self, mat, target):
        rows=len(mat)
        cols=len(mat[0])
        left=0
        right=rows*cols-1
        while left<=right:
            mid=(left+right)//2
            row=mid//cols
            col=mid%cols
            if mat[row][col]== target:
                return True
            elif mat[row][col]<target:
                left=mid+1
            else:
                right=mid-1
        return False
