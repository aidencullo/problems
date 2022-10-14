#include <iostream>
#include <vector>
#include "file.h"
using namespace std;

int Solution::largestPerimeter(vector<int>& nums) {
  sort(nums.begin(), nums.end());
  for(int i = nums.size(); i > 1; i--){
    int a = nums[i-2];
    int b = nums[i-1];
    int c = nums[i];
    if(a+b > c && a+c > b && b+c > a){
      return a+b+c;
    }
  }
  return 0;
};
