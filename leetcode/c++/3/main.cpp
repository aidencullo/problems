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
  s.execute(vect1);
  cout << "expectation: 1  --- output:" <<  endl;
  s.execute(vect2);
  cout << "expectation: 3  --- output:" <<  endl;
  s.execute(vect3);
  cout << "expectation: 10  --- output:" <<  endl;
  s.execute(vect4);
  return 0;
  
}

