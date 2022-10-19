#include <iostream>
#include <vector>
#include "file.h"
using namespace std;

int main(){

  cout << "Testing...." << endl;
  Solution s;
  vector<int> vect1{2,1,2};
  vector<int> vect2{1,2,1};
  vector<int> vect3{0,0,0};
  vector<int> vect4{3,2,3,4};
  cout << "expectation: 5  --- output:"<<endl;
  s.largestPerimeter(vect1);
  cout << "expectation: 0  --- output:" <<  endl;
  s.largestPerimeter(vect2);
  cout << "expectation: 0  --- output:" <<  endl;
    s.largestPerimeter(vect3);
    cout << "expectation: 10  --- output:" <<  endl;
  s.largestPerimeter(vect4);
  return 0;
  
}

