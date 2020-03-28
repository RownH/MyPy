#  循环队列测试
class queue(object):
    def __init__(self,maxlen):
        self.m_max=maxlen;
        self.m_list=[0 for i in range(0,maxlen)];
        self.m_list;
        self.front=0;
        self.trail=0;
    def empty(self):
        return self.front==self.trail;
    def full(self):
        return (self.front+1)%self.m_max==self.trail;
    def push(self,val):
        if self.full():
            return False;
        else:
            self.m_list[self.front]=val;
            self.front=(self.front+1)%self.m_max;
        return True
    def top(self):
        if not self.empty():
            return self.m_list[self.front-1];
        return None
    def back(self):
        if not self.empty():
            return self.m_list[self.trail];
        return None
    def pop(self):
        if self.empty():
            return False;
        else:
            self.trail=(self.trail+1)%self.m_max;
    def list(self):
        return [str(self.m_list[x]) for x in range(self.trail%self.m_max,self.front%self.m_max)];
    def __str__(self):
        a=[str(self.m_list[x]) for x in range(self.trail%self.m_max,self.front%self.m_max)]
        return ' '.join(a);
q=queue(101);
for i in range(98):
    q.push(i);
print(q.full())
