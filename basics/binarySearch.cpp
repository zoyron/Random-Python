#include <bits/stdc++.h>
using namespace std;

int binarySearch(int *arr, int target){
  int left = 0, right = 9;
  while(left <= right){
    int mid = (left + right)/2;
    if(arr[mid] == target)
      return mid;
    else if(arr[mid] < target)
      left = mid + 1;
    else
      right = mid - 1;
  }
  return -1;
}

int main(){
  int arr[10] = {1,2,3,4,5,6,7,8,9,10};
  int ans = binarySearch(arr, 7);
  if(ans!=-1)
    cout << "The target is at the index " << ans << " in the array" << endl;
  else
    cout << "The target is not present in the array\n";
  return 0;
}

