import sys
import os
sys.path.append(os.getcwd()+'/programerTest/test2/')
import unittest  # 导入unittest  包
from queue import queue

class queue_test(unittest.TestCase):
   def setUp(self):
       print('初始化')
       self.quene=queue(100+1);
   def test_push(self):
       for i in range(100):
           self.quene.push(i);
           self.assertEqual(self.quene.top(),i);

   def test_pop(self):
       for i in range(100):
           self.quene.push(i);
       for i in range(100):
           self.assertEqual(self.quene.back(),i);
           self.quene.pop();
   def test_empty(self):
       print('---测试用例 empty---')
       self.assertEqual(self.quene.empty(),1);
   def test_full(self):
       for i in range(100):
           self.quene.push(i);
       print('---测试用例 full---')
       self.assertEqual(self.quene.full(),1);
   def tearDown(self):
       print('结束')

def suite():  # 创建测试添加测试套件函数
   suite = unittest.TestSuite()  # 建立测试套件
   suite.addTests([queue_test('test_empty'), queue_test('test_push'),queue_test('test_full'),queue_test('test_pop'),queue_test('test_empty')])
   return suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(suite())