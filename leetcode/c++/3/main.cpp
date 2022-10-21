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
  cout << "expectation: 3  --- output:"<<endl;
  s.execute(input1);
  cout << "expectation: 1  --- output:" <<  endl;
  s.execute(input2);
  cout << "expectation: 3  --- output:" <<  endl;
  s.execute(input3);
  cout << "expectation: 10  --- output:" <<  endl;
  s.execute(input4);
  return 0;
  
}

