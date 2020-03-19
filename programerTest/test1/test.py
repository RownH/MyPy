#代码片段1，测试用例创建
import sys
import os
import unittest
 
sys.path.append(os.getcwd()+'/programerTest/test1/')
print(sys.path)
from quickSort import quickSort;
from heapSort import heapSort;
from mergeSort import mergeSort;
class Test_Math(unittest.TestCase):
    #每执行一个用例，都会执行setup()和teardown()方法
    #如果跑所有用例，只运行一次前提条件和结束条件。则用setupclass()和teardownclass()
    def setUp(self):
        print("测试用例执行前的初始化操作========")
     def tearDown(self):
        print("测试用例执行完之后的收尾操作=====")
    def test_SortByquick_01(self):
        nums=[3,1,2,5,6,7,8,10,2,4]
        quickSort(nums,0,len(nums)-1)
        self.assertEqual([1,2,2,3,4,5,6,7,8,10],nums);
    def test_SortByMerge(self):
        nums=[3,1,2,5,6,7,8,10,2,4]
        mergeSort(nums,0,len(nums)-1)
        self.assertEqual([1,2,2,3,4,5,6,7,8,10],nums);
    def test_SortByHeap(self):
        nums=[3,1,2,5,6,7,8,10,2,4]
        heapSort(nums,len(nums)-1)
        self.assertEqual([1,2,2,3,4,5,6,7,8,10],nums);
if __name__ == '__main__':  
    unittest.main()