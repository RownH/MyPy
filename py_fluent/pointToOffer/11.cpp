class Solution {
public:
    int minArray(vector<int>& numbers) {
        int left = 0;
        int right = numbers.size() - 1;
        int min = INT_MAX;
        while (left <= right) {
            int middle = left + ((right - left) >> 1);
            if (numbers[middle] < min) {
                min = numbers[middle];
            }
            if (numbers[right] > numbers[middle]) {
                right = middle - 1;
            }
            else if(numbers[right]==numbers[middle]){
                --right;
            }
            else {
                left = middle + 1;
            }
        }
        return min;
    }
};