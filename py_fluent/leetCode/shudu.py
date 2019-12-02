import time  # 倒入时间模块
t0 = time.time()  # 启动程序时间


class point:  # 点
    def __init__(self, x, y):  # 构造函数
        self.x = x  # 初始化x,y
        self.y = y
        self.available = []  # 可选的点
        self.value = 0  # 值默认为0


def rowNum(p, sudoku):
    row = set(sudoku[p.y*9:(p.y+1)*9])  # 取得p所在当前一行 set
    row.remove(0)  # 除去第0项
    return row  # 返回set(row)


def colNum(p, sudoku):
    col = []
    length = len(sudoku)    #获得整个数组的大小
    for i in range(p.x, length, 9): 
        col.append(sudoku[i])   #获得当前点的 p所在的一列
    col = set(col)  #去除重复值
    col.remove(0)#去除0值
    return col  #返回当前


def blockNum(p, sudoku): #取得x所属块的值
    block_x = p.x//3    #当前x余3
    block_y = p.y//3    #当前y余3
    block = []
    start = block_y*3*9+block_x*3   #获得当前块的左上角点
    for i in range(start, start+3):
        block.append(sudoku[i]) #将第一行的值 放入数组
    for i in range(start+9, start+9+3): #第二行值 放入
        block.append(sudoku[i])
    for i in range(start+9+9, start+9+9+3):#第三行值
        block.append(sudoku[i])
    block = set(block)  #去除重复值
    block.remove(0) #去除0值
    return block  # set type


def initPoint(sudoku):  # 初始化
    pointList = []  # 创建一个列表
    length = len(sudoku)  # 获取数独剧组的总大小
    for i in range(length):  # 遍历0-80个元素
        if sudoku[i] == 0:  # 如果这个点上没有值
            p = point(i % 9, i//9)    # y为 此点除9  x为此点余9
            for j in range(1, 10):  # 遍历9次 1 -9 之间 选择值放入可备用数组中
                if j not in rowNum(p, sudoku) and j not in colNum(p, sudoku) and j not in blockNum(p, sudoku):  # 如果1-9递增的值  不再当前行  当前列  当前块中
                    p.available.append(j)   #把这个值放入数组中
            pointList.append(p)    #把整个数组添加进数组中
    return pointList #返回整个数组中 每一项为0的点 坐标值以及为可选的点


def tryInsert(p, sudoku):
    availNum = p.available  
    for v in availNum:
        p.value = v
        if check(p, sudoku):
            sudoku[p.y*9+p.x] = p.value #把该点放入在数组中
            if len(pointList) <= 0: #如果当前队列中已经不存在点
                t1 = time.time()    #获得结束时间
                useTime = t1-t0     #两次时间相减
                showSudoku(sudoku)  #显示递归后的结果
                print('\nuse Time: %f s' % (useTime))   #显示使用时间
                exit()  #退出
            p2 = pointList.pop()    #弹出第二个点
            tryInsert(p2, sudoku)   #递归插入 插入第二个点
            sudoku[p2.y*9+p2.x] = 0 #数独的第(y,x)点和(x,y)点 赋值为0 如果有一次插入失败时 需要递归 修改之前状态为0
            sudoku[p.y*9+p.x] = 0
            p2.value = 0    #值为0
            pointList.append(p2)    #将p2添加至末尾
        else:   #重新加入
            pass


def check(p, sudoku):
    if p.value == 0:    #如果当前点为0 返回没有值给点p
        print('not assign value to point p!!')
        return False
    if p.value not in rowNum(p, sudoku) and p.value not in colNum(p, sudoku) and p.value not in blockNum(p, sudoku):
        return True     #如果该值不存在于 当前行  或者 当前列  或者当前所属的块时  返回True
    else:
        return False    #否则返回假


def showSudoku(sudoku):
    for j in range(9):
        for i in range(9):
            print('%d ' % (sudoku[j*9+i]), end='')
        print('')


if __name__ == '__main__':
    sudoku = []  # 数独列表
    for _ in range(0,81):
        temp=int(input());
        sudoku.append(temp);

    pointList = initPoint(sudoku)   #初始化每个点  大概能放那些值
    showSudoku(sudoku)  #打印出当前数组的样子
    print('\n')
    p = pointList.pop() #弹出最后一项
    tryInsert(p, sudoku)    #递归插入点
