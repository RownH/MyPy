class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<0:
            return False
        if num==1:
            return True;
        if num<4:
            return False
        if num==4:
            return True
        snum=str(bin(num))
        index=len(snum)-snum.find('1')-2
        snum[snum.find('1')]='0';
        if int(snum]='0')==0:
            if index%3==0:
                return True
        else:
            return False;