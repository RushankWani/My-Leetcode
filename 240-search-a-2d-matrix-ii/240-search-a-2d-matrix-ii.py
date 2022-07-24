class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for arr in matrix:
            start=arr[0]
            if target>=start:
                if target in arr:
                    return True
        return False
        
        