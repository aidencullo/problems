#include <iostream>
#include <string>
#include "solution.h"
using namespace std;

int Solution::execute(string input) {
  string str;
  int ind = 0;
  int max = 0;
  for(char c : input){
    ind  = str.find(c);
    if (ind == std::string::npos) {
      str = str + c;
    } else {
      str = str.substr(ind+1) + c;
    }
    if(str.size() > max){
      max = str.size();
    }
  }
  return max;
};
