'''
345. 反转字符串中的元音字母




题目描述
评论 (170)
题解(43)New
提交记录
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:

输入: "hello"
输出: "holle"
示例 2:

输入: "leetcode"
输出: "leotcede
'''
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        lists=list(s)
        if len(lists)==0:
            return ''
        nums=['a','e','i','o','u'];
        i=0
        j=len(lists)-1;
        print(i,j)
        while i<j:
            while i<=j:
                if lists[i].lower() in nums:
                    print(lists[i])
                    break;
                else:
                    i+=1;
            while j>=i:
                if lists[j].lower() in nums:
                    lists[i],lists[j]=lists[j],lists[i]
                    print(lists[i:j+1])
                    i+=1;
                    j-=1;
                    break;
                else:
                    j-=1;       
        return ''.join(lists);
        
a=Solution();
print(a.reverseVowels('hello'));
