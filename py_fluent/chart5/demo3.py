'''
    5.3 匿名函数
    lambda关键字在Python表达式内创建匿名函数

    python简单的语法限制了lambda函数的定义体不能赋值 也不能使用while和try等python语句


'''
def example():
    fruits=['strawberry','fig','apple','cherry','raspberry','banana']
    print(sorted(fruits,key=lambda word:word[::-1]))
example()
