def heapfy(nums,i,len):
    while True:
        maxPos=i;
        if i*2 <len and nums[i]<nums[i*2+1]:
            maxPos=2*i+1;
        if i*2+2<len and nums[maxPos]<nums[i*2+2]:
            maxPos=2*i+2;
        if maxPos==i:
            break;
        nums[i],nums[maxPos]=nums[maxPos],nums[i]
        i=maxPos
def buildheap(nums,len):
    for i in range((len-1)//2,-1,-1):
        heapfy(nums,i,len);
def heapSort(nums,len):
    buildheap(nums,len);
    k=len
    while True:
        nums[0],nums[k]=nums[k],nums[0]
        k-=1
        if k==0:
            return
        heapfy(nums,0,k);
