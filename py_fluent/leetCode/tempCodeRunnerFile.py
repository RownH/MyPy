class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sum=0;
        for i in grid:
            for j in i:
                sum+=self.count(grid,i,j);
        return sum;

    def count(grid,i,j):
        cnt=0;
        if grid[i][j]==0:
            return 0;
        else:
            if i==0 || grid[i-1][j]==0:
                cnt+=1;
            if i==len(grid[i])-1 || grid[i+1][j]==0:
                cnt+=1;
            if j==0||grid[i][j-1]==0:
                cnt+=1;
            if j==len(grid)-1 || grid[i][j+1]==0:
                cnt+=1;
        return cnt;