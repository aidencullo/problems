#include <stdio.h>
#include "solution.h"

int main(int argc, char *argv[]) {

  printf("Testing....\n");
  int input1 = 123;
  int input2 = -123;
  int input3 = 120;
  int input4 = 1534236469;
  int input5 = -2147483412;
  printf("expectation: 321  --- output: %d\n", execute(input1));
  printf("expectation: -321  --- output: %d\n", execute(input2));
  printf("expectation: 21  --- output: %d\n", execute(input3));
  printf("expectation: 0  --- output: %d\n", execute(input4));
  printf("expectation: -2143847412  --- output: %d\n", execute(input5));

  return 0;

}
