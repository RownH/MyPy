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
        list=[];
        for i in range(0,12):
            for j in range(0,60):
                if self.count(i)+self.count(j)==num:
                    s="{}:{:0>2d}".format(i,j);
                    list.append(s);
        return list;
    def count(self,num):
        res=0;
        while num!=0:
            num=num&(num-1)
            res+=1;
        return res;
                
a=Solution();
print(a.readBinaryWatch(3))