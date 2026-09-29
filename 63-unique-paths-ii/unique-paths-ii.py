class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0]==1:
            return 0
        rows,cols=len(obstacleGrid),len(obstacleGrid[0])
        obstacleGrid=[[0]*cols]+obstacleGrid
        obstacleGrid=[[0]+r for r in obstacleGrid]
        obstacleGrid[1][1]=1
        for r in range(1,rows+1):
            for c in range(1,cols+1):
                if r==1 and c==1:
                    continue
                if obstacleGrid[r][c]==1:
                    obstacleGrid[r][c]=0
                else:
                    obstacleGrid[r][c]=obstacleGrid[r-1][c]+obstacleGrid[r][c-1]
        return obstacleGrid[rows][cols]



        




        # if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1:
        #     return 0
        
        # m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # previous = [0] * n
        # current = [0] * n
        # previous[0] = 1
        
        # for i in range(m):
        #     current[0] = 0 if obstacleGrid[i][0] == 1 else previous[0]
        #     for j in range(1, n):
        #         current[j] = 0 if obstacleGrid[i][j] == 1 else current[j-1] + previous[j]
        #     previous[:] = current
        
        # return previous[n-1]