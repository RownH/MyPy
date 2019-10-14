'''
    401. 二进制手表




题目描述
评论 (149)
题解(34)New
提交记录
二进制手表顶部有 4 个 LED 代表小时（0-11），底部的 6 个 LED 代表分钟（0-59）。

每个 LED 代表一个 0 或 1，最低位在右侧。



例如，上面的二进制手表读取 “3:25”。

给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。

'''
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        minute=[1,2,4,8,16,32,60,120,240,480]
        method=[[]];
        for _ in range(0,num):
