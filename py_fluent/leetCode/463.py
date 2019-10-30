'''
    463. 岛屿的周长




题目描述
评论 (136)
题解(35)New
提交记录
给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。

网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。

岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。
'''
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
            

