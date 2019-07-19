def main():
    f=None
    try:
        with open('test.txt','r',encoding='utf-8') as f:
             print(f.read())
    except FileNotFoundError:
        print('file not find')
    except LookupError:
        print('指定未知编码')
    except UnicodeEncodeError:
        print('读取文件错误')
    finally:
        if f:
            f.close()
if __name__=='__main__':
    main()