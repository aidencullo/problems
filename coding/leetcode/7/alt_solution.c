#include <math.h>
#include <limits.h>
#include <stdio.h>
#include "solution.h"

int execute(int in) {
  long input = in;
  int sign=1;
  int i;
  long result=0;
  int digit = 0;
  if(input < 0){
    sign = -1;
    input = input*-1;
  }
  for(i=0; i < 10 && input > 0; i++){
    result = result * 10;
    digit = input - (input/10)*10;
    result = result + digit;
    input  = input / 10;
    if(result >= INT_MAX){
      return 0;
    }
  }
  return result * sign;
};
