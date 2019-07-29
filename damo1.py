from random import randint
def Probability(n,m,k):
    num={"red":n,"green":m,"yellow":k}
    while True:
        if num['red']+num['green']+num['yellow']==1:
            if num['red']==1:
                return "red"
            elif num['green']==1:
                return "green"
            else:
                return "yellow"
        i=randint(0,2)
        if i==0:    #当摇处红色
            continue;
        elif i==1:
            if num['green']==0:
                continue
            else:
                num['green']-=1; 
                if num['red']+num['green']+num['yellow']==1:
                    if num['red']==1:
                        return "red"
                    elif num['green']==1:
                        return "green"
                    else:
                        return "yellow"
                else:
                    while True:
                        s=randint(0,2);
                        if s==0 and num['red']!=0:
                            num['red']-=1;
                            break;
                        elif s==1 and num['green']!=0:
                            num['green']-=1;
                            break;
                        elif s==2 and num['yellow']!=0:
                            num['yellow']-=1;
                            break;
                        else:
                            continue
        elif i==2:
            if num['yellow']==0:
                continue;
            else:
                num['yellow']-=1;

if __name__=="__main__":
    m,n,k=0,0,0;
    i=1;
    j=int(input('请输入绿球个数?'));
    s=int(input('请输入黄球个数?'));

    for _ in range(0,10000):
        result=Probability(i,j,s)
        if result=="red":
            m+=1;
        elif result=="green":
            n+=1;
        elif result=="yellow":
            k+=1;
        else:
            print("出现错误")
    acount=m+n+k;
    pa=m/acount;
    pb=n/acount;
    pc=k/acount;
    print("red %0.3f  green %0.3f yellow %0.3f"%(pa,pb,pc))             