#include <iostream>
#include <string>
#include "solution.h"
using namespace std;

int main(){

  cout << "Testing...." << endl;
  Solution s;
  string input1 = "abcabcbb";
  string input2 = "bbbbb";
  string input3 = "pwwkew";
  string input4 = "abcdefghij";
  cout << "expectation: 3  --- output:" << s.execute(input1) << endl;
  cout << "expectation: 1  --- output:" << s.execute(input2) << endl;
  cout << "expectation: 3  --- output:" << s.execute(input3) << endl;
  cout << "expectation: 10  --- output:" << s.execute(input4) << endl;
  return 0;
  
}

