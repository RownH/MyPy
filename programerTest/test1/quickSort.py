def quickSort(nums,Left,Right):
      left=Left;
      right=Right;
      if left>=right:
          return ;
      temp=nums[left];
      while left<right:
          while left<right and nums[right]>=temp:
              right-=1;
          nums[left]=nums[right];
          while left<right and nums[left]<temp:
              left+=1;
          nums[right]=nums[left];
      nums[left]=temp;
      quickSort(nums,Left,left-1);
      quickSort(nums,right+1,Right);

