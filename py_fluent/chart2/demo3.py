'''
2.5 对序列使用+和*
python程序员默认序列是支持+和*操作的,通常+号两侧的序列时由相同类型数据构成
'''

def example251():
    l=[1,2,3]
    print(l*5) #5份拼接

    #如果m*n  m内有对对象的引用,则n个引用指向同一个列表,  [[]] 内是一个引用
def example252():
    #由列表组成的列表
    board=[['_']*3 for i in range(3)]
    print(board)
    board[1][2]='x';
    print(board)

    #等价于
    board1=[];
    for i in range(3):
        row=['_']*3;
        board1.append(row);
    board1[1][1]='X'
    print(board1)

    #错误操作
    board2=[['_']*3]*3
    print(board2)
    board2[1][2]='X';
    print(board2)
    #错误等价于
    row=['_']*3
    bord3=[]
    for i in range(3):
        bord3.append(row)
    bord3[1][2]='X'
    print(bord3)
example251()
example252()