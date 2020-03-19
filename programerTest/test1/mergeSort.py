def merge(nums,left,middle,right):
    temp=list()
    i=left
    j=middle+1;
    k=0;
    while i<=middle and j<=right:
        if nums[i]<=nums[j]:
            temp.append(nums[i]);
            i+=1
        else:
            temp.append(nums[j]);            
            j+=1;
    while i<=middle:
        temp.append(nums[i]);
        i+=1
    while j<=right:
        temp.append(nums[j]);
        j+=1;
    k=0;       
    while left<=right:
        nums[left]=temp[k];
        left+=1; 
        k+=1;
        

def mergeSort(nums,left,right):
    if left>=right:
        return ;
    midlie=(left+right)//2;
    mergeSort(nums,left,midlie);
    mergeSort(nums,midlie+1,right);
    merge(nums,left,midlie,right);