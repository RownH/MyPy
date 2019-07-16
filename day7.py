import sys
def main():
    str1='hello,world!'
    print(len(str1))
    print(str1.capitalize())
    print(str1.upper())
    print(str1.find('or'))
    print(str1.startswith('he'))
    print(str1.endswith('world!'))
    print(str1.center(50,'*'))
    print(str1[2:5])
    print(str1[2:])
    print(str1[2::2])
    print(str1[::2])
    print(str1[-2::-1])
    print(str1[-3:-1])

def test2():
    fruits=['graoe','apple','strawberry','waxberry']
    fruits +=['pitaya','pear','mango']
    for fruit in fruits:
        print(fruit,end=' ')
    print();
    fruits2=fruits[1:4]
    print(fruits2)
    fruits3=fruits[:]
    print(fruits3)
    fruit4=fruits[::-1];
    print(fruit4)
def test3():
        list1=['brange','apple','coo','dasasd','blueberry']
        list2=sorted(list1)
        list3=sorted(list1,reverse=True)
        list4=sorted(list1,key=len)
        print(list1)
        print(list2)
        print(list3)
        print(list4)
def test4():
    f=[x for x in range(1,10)]
    print(f)
    f=[x+y for x in 'ABCDE' for y in '1234567']
    print(f)
    f=[x**2 for x in range(1,10)]
    print(sys.getsizeof(f))
    print(f)
def test5():
    t=('rh',38,True,'chengdu')
    print(t[0])
    print(t[1])
    for member in t:
        print(member)
    print(t)
    person=list(t);
    person[0]=2;
    print(person);
if __name__=='__main__':
    test5();