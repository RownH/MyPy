class Solution:
    def compareVersion(self , version1 , version2 ):
        # write code here
        list1=version1.split('.');
        list2=version2.split('.');
        shortlen=0;
        if len(list1)>len(list2):
            shortlen=len(list2);
        else:
            shortlen=len(list1);
        for i in range(0,shortlen):
            if int(list1[i])>int(list2[i]):
                print(1);
                return 1;
            elif int(list1[i])<int(list2[i]):
                print(-1);
                return -1;
            else:
                pass
        if len(list1)==len(list2):
            print(0);
            return -1;
        if len(list1)>len(list2):
            shuzu=[int(list1[x]) for x in range(len(list2),len(list1))]
            if max(shuzu)!=0:
                print(1)                
                return 0;
            print(0);
        else:
            shuzu=[int(list2[x]) for x in range(len(list1),len(list2))]
            if max(shuzu)!=0:
                print(-1)                
                return 0;
            print(0);
a=Solution();
a.compareVersion('1.0.1','1.0.0.1');