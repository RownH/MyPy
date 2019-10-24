class Person:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
    def getPay(self):
        pass;
    def print(self):
        pass;
class Manager(Person):
    def __init__(self,name,age,pay):
        super().__init__(name,age);
        self.pay=pay;
    def getPay(self):
        self.count=self.pay;
        return self.pay;
    def print(self):
        print(self.name);
        print(self.age);
        print(self.pay);


class Employee(Person):
    def __init__(self,name,age,price,yearPrice):
        super().__init__(name,age);
        self.pay=price;
        self.yearPrice=yearPrice;
    def getPay(self):
        self.count=self.pay*12+self.yearPrice;
        return self.count;
    def print(self):
        print(self.name);
        print(self.age);
        print(self.count);

class SaleMan(Person):
    def __init__(self,name,age,price,yearPrice):
        super().__init__(name,age);
        self.pay=price;
        self.yearPriceRate=yearPrice;
    def getPay(self):
        self.count=self.pay*12+self.yearPriceRate*0.15;
        return self.count;
    def print(self):
        print(self.name);
        print(self.age);
        print(self.count);

a=SaleMan('Tom',25,5000,1000000);
a.getPay();
a.print();
b=Manager('Alice',20,500000);
b.getPay();
b.print();

c=Employee('Bob',23,10000,60000);
c.getPay();
c.print();
if __name__ == "__main__":
    postion=input('请输入职务:');
    if postion=='Manager':
        name=input('请输入姓名:');
        age=input('请输入年龄:');
        example=Manager(name,age,500000);
    elif postion=='Employee':
        name=input('请输入姓名:');
        age=input('请输入年龄:');
        price=int(input('请输入月薪:'));
        yearsPrice=int(input('请输入年终奖'));
        example=Employee(name,age,price,yearPrice);
    elif postion=='SaleMan':
        name=input('请输入姓名:');
        age=input('请输入年龄:');
        price=int(input('请输入月薪:'));
        yearsPrice=float(input('请输入年销售率'));
        example=Employee(name,age,price,yearPrice);
    else:
        print('职位不存在 清重新打开');
    example.getPay();
    example.print();