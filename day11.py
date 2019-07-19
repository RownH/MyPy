def main():
    f=None
    try:
        with open('test.txt','r',encoding='utf-8') as f:
            lines=f.readlines()
            print(lines)    #单行读取

    except FileNotFoundError:
        print('file not find')
    except LookupError:
        print('指定未知编码')
    except UnicodeEncodeError:
        print('读取文件错误')
    finally:
        if f:
            f.close()
def writFile():
    filenames=('C://Users/罗/Documents/GitHub/MyPy/a.txt','C:/Users/罗/Documents/GitHub/MyPy/b.txt','C:/Users/罗/Documents/GitHub/MyPy/c.txt')
    file_list=[]
    try:

        for filename in filenames:
            file_list.append(open(filename,'w',encoding='utf-8')) 
        for x in range(0,10000,2):
            if x<100:
                file_list[0].write(str(x)+'\n')
            elif x<1000:
                file_list[1].write(str(x)+'\n')
            else:
                file_list[2].write(str(x)+'\n')
    except IOError as ex:
        print(ex)
        print('写文件错误')
    finally:
        for fs in file_list:
            fs.close()
    print('操作完成')
def main1():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
             if number < 100:
                fs_list[0].write(str(number) + '\n')
             elif number < 1000:
                fs_list[1].write(str(number) + '\n')
             else:
                fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件时发生错误!')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成!')

if __name__=='__main__':
    writFile()