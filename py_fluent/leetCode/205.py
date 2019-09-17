'''
    205 同构字符串
New

给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
还有一个方法  判断
'''
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for _ in  range(0,len(s)):
            if s[_] in s[0:_]:
                continue
            print(self.isSimple(s,s[_]),self.isSimple(t,t[_]))
            if self.isSimple(s,s[_])!=self.isSimple(t,t[_]) :
                return False;
        return True                        
            
    def isSimple(self,s,i):
        nums=[d for d in range(0,len(s)) if s[d]==i]
        return nums;    #此为一个方法

s=Solution();
print(s.isIsomorphic('abba','abab'))
