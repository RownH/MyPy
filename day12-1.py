from time import sleep
from threading import Thread,Lock
class Acount(object):
    def __init__(self):
        self._balance=0
        self._lock=Lock()
    def deposit(self,money):
        self._lock.acquire()
        try:
            new_balance=self._balance+money
            sleep(0.01)
            self._balance=new_balance
        finally:
            self._lock.release()
    @property
    def balance(self):
        return self._balance

class AddMoneyThread(Thread):
    def __init__(self,account,money):
        super().__init__()
        self._account=account
        self._money=money
    def run(self):
        self._account.deposit(self._money) 
def main():
    accout=Acount()
    threads=[]
    for _ in range(100):
        t=AddMoneyThread(accout,1)
        threads.append(t)
        t.start()
    for _ in threads:
        _.join()
    print('账户余额为:$%d'%accout.balance)

if __name__=='__main__':
    main();