class MyTterator:
     def __init__(self,x=6):
        self._x=x
        self.index=3;
     def __iter__(self):
         return self;

     def __next__(self):
        for i in range(self.index, self._x):
            for j in range(2, i + 1):
                     if i % j==0:
                         pass;
                     else:
                        return  i
        raise StopIteration

itera=MyTterator(x=10)
for _ in itera:
    print(_);