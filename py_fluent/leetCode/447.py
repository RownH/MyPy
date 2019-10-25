'''
447. 回旋镖的数量




题目描述
评论 (83)
题解(12)New
提交记录
给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。

示例:

输入:
[[0,0],[1,0],[2,0]]

输出:
2

解释:
两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
'''
from collections import Counter;
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def f(x,y):
            d=Counter((x1-x)**2+(y1-y)**2 for x1,y1 in points);
            return sum(t*t-t for t in d.values())
        return sum(f(x,y) for x,y in points);
        