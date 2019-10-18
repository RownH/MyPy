'''
程序的功能包括：学生信息的录入、修改、查询、按总分降序排列四个功能。

每个学生的信息包括：学号、姓名、数学成绩、语文成绩、英语成绩共5项信息

程序运行后的第一层交互界面如下：

1. 学生成绩录入

2. 学生成绩修改

3. 查询学生成绩

4. 学生成绩排名

5. 退出系统

输入1-4回车进入具体功能的交互界面（交互界面自行设计），输入5回车，程序退出。

要求：

（1）使用二维列表存储多名学生的成绩数据

（2）1-4的每个功能执行完毕后要返回到主界面，可自动返回到主界面，也可以通过交互返回到主界面

（3）学生成绩录入功能中，学号和已有学生的学号不允许重复

（4）学生成绩修改功能中，学号不能修改，姓名和各科成绩均可修改

（5）学生成绩查询功能中，用户输入学号或姓名均可查询到学生信息，如果有重复名字的同学都要输出
'''
students=[]  ;#全局变量 存放学生信息
def entryStudent():
    while True:
        ids=int(input('请输入学号:'));
        isT=0;
        for _ in students:
            if _[0]==ids:
                isT=1;#判断是否有相同学号
                print('学号重复 请重新输入!')
                break;
        if isT:
            continue;                
        student=[];#学生信息列表
        name=input('请输入姓名:');
        math=int(input('请输入数学成绩:'));
        chinese=int(input('请输入语文成绩:'));
        english=int(input('请输入英语成绩:'));
        student.append(ids);
        student.append(name);
        student.append(math)
        student.append(chinese)
        student.append(english);
        student.append(math+chinese+english);#总分也存入数组中
        students.append(student);
        n=int(input('是否继续录入学生信息 1 是  其他键返回'));
        if n!=1:
            return;
def updateStudent():
    n=int(input('你想修改学号为多少的学生信息:'));
    exist=0;
    for _ in range(0,len(students)):
        if students[_][0]==n:
            exist=1;#判断是否有相同学号
            n=_;#在第几个位置 副值给n
            break;
    if exist==0:
        print('当前学号不存在 无法修改');
        return;
    else:
        while True:
            c=int(input('下列请输入你想修改的信息: 1 姓名 2 数学成绩 3 语文成绩 4 英语成绩 其他键退出'))
            if c==1:
                students[n][1]=input('修改后的姓名为:')
            elif c==2:
                students[n][2]=int(input('修改后的数学成绩为:'))
                students[n][5]=sum(students[n][2:5]);
            elif c==3:
                students[n][3]=int(input('修改后的语文成绩为:'))
                students[n][5]=sum(students[n][2:5]);
            elif c==4:
                students[n][4]=int(input('修改后的英语成绩:'))
                students[n][5]=sum(students[n][2:5]);
            else:
                return ;
            
def findStudent():
    while True:
        n=int(input('通过 1 学号查询 2 姓名查询 其他 退出' ));
        if n==1:
            ids=int(input('你要查找的学号为'));
            exist=0;
            for _ in range(0,len(students)):
                if students[_][0]==ids:
                    exist=1;#判断是否有相同学号
                    ids=_;#在第几个位置 副值给n
                    break;
            if exist==0:
                print('当前学号不存在 请检验后输入');
            else:
                print('学号{} 姓名{} 数学成绩{} 语文成绩{} 英语成绩{}'.format(students[ids][0],students[ids][1],students[ids][2],students[ids][3],students[ids][4]))
        elif n==2:
            ids=input('你要查找的姓名为');
            exist=0;
            lists=[];
            for _ in range(0,len(students)):
                if students[_][1]==ids:
                    lists.append(students[_])
            if len(lists)==0:
                print('当前姓名不存在 请检验后输入');
            else:
                for s in lists:
                    print('学号{} 姓名{} 数学成绩{} 语文成绩{} 英语成绩{}'.format(s[0],s[1],s[2],s[3],s[4]))
        else:
            return ;
def sortStudent():
    students.sort(key=(lambda x: x[5]),reverse=True)


def mainWindow():
    print('1. 学生成绩录入');
    print('2. 学生成绩修改');
    print('3. 查询学生成绩');
    print('4. 学生成绩排名');
    print('5. 退出系统');

def main():
    while True:
        mainWindow();
        n=int(input('请输入选项:'));
        if n==1:
            entryStudent();
            print(students);
        elif n==2:
            updateStudent();
            print(students)
        elif n==3:
            findStudent();
        elif n==4:
            sortStudent();
            for s in students:
                print('学号{} 姓名{} 数学成绩{} 语文成绩{} 英语成绩{} 总分{}'.format(s[0],s[1],s[2],s[3],s[4],s[5]))
        elif n==5:
            return;
        else:
            print('请选择以下选项')
            

if __name__ == "__main__":
    main()