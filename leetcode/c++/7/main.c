#include <stdio.h>
#include "solution.h"

int main(int argc, char *argv[]) {

  printf("Testing....\n");
  Solution s;
  int input1 = 123;
  int input2 = -123;
  int input3 = 120;
  printf("expectation: 321  --- output: %d", s.execute(input1));
  printf("expectation: -321  --- output: %d", s.execute(input2));
  printf("expectation: 21  --- output: %d", s.execute(input3));
  return 0;
  
}

