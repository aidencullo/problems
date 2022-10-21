#include <iostream>
#include <string>
#include "solution.h"
using namespace std;

int Solution::execute(string input) {
  string substr;
  for(auto c : input){
    int i = 0;
    int included = 0;
    while(i < substr.size()){
      if(c == substr[i]){
	included = 1;
	break;
      }
      i++;
    }
    if(included == 0){
      substr = substr + c;
    }
  }
  return substr.size();
};
