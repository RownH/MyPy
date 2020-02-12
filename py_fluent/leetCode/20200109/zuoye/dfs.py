JZ=[];#创建矩阵
star_point=0;#起点和终点都设置为0
end_point=0;
result=[];#保存结果
def init():
    with open('a.text','r',encoding='utf8') as f:
        border=int(f.readline().strip(' ')); #边数数
        point=int(f.readline().strip(' '));#顶点数
        for _ in range(0,point):
            JZ.append([0]*point)
        for _ in range(0,border):
            form,to=f.readline().strip(' ').split(' ')
            JZ[int(form)-1][int(to)-1]=1;
            JZ[int(to)-1][int(form)-1]=1 #双向的
            global star_point;
            global end_point;
        star_point=int(f.readline().strip(' '))-1;
        end_point=int(f.readline().strip(' '))-1;
        print(JZ)

def DFS(cus,path):  #深度优先遍历  递归  记录当前点信息 和目的点信息 传入路径
    path.append(cus)
    if cus==end_point:
        result.append(path)
        return;
    else:
        for _ in range(0,len(JZ[cus])):
            if JZ[cus][_]==0:
                pass;
            else:
                if _ not in path:
                    DFS(_,path.copy());
                else:
                    pass;




init();
DFS(star_point,[]);
print(result)
for _ in result:
    for n in _:
        print(n,end='');
    print();
