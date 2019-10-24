
import sqlite3


def creatDateBase(name):
       conn = sqlite3.connect('{}.db'.format(name))
       print("Opened database successfully");
       c = conn.cursor()
       c.execute('''CREATE TABLE student
              (ID INT PRIMARY KEY     NOT NULL,
              NAME           TEXT    NOT NULL,
              CHINESE         INT     NOT NULL,
              MATH        INT     NOT NULL,
              ENGLISH     INT     NOT NULL,
              COUNT     INT     NOT NULL);''')
       print("Table created successfully");
       conn.commit()


def insetStudent(id, name, chinese, math, english, count):
       try:
              conn = sqlite3.connect('test.db')
              c = conn.cursor()
              c.execute("INSERT INTO student (ID,NAME,CHINESE,MATH,ENGLISH,COUNT) \
              VALUES ({}, '{}', {}, {}, {},{} )".format(id, name, chinese, math, english, count));
              conn.commit()
       except sqlite3.IntegrityError:
              print('已存在学号{}'.format(id));
       else:
              print('成功')
       conn.close()


def sortedStudent():
       try:
              conn = sqlite3.connect('test.db')
              c = conn.cursor()
              cursor = c.execute("select * from student order by COUNT");
              for row in cursor:
                     for _ in row:
                            print(_, end=' ');
                     print();
       conn.commit()
def selectName(name):
       conn = sqlite3.connect('test.db')
       c = conn.cursor()
       cursor=c.execute("select * from student where NAME='{}'".format(name));
       for row in cursor:
              for _ in row:
                     print(_,end=' ');
                     print();
              conn.commit()


