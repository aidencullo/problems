#include <math.h>
#include <limits.h>
#include <stdio.h>
#include "solution.h"

int execute(int in) {

  long input = in;
  int sign=1;
  int num[10]={0};
  int i;
  long result=0;
  long result_addition=0;
  if(input < 0){
    sign = -1;
    input = input*-1;
  }
  // loop through int and capture each digit in array
  for(i=0; i < 10 && input > 0; i++){
    num[i] = input - (input/10)*10;
    input  = input / 10;
  }
  i = i-1;
  // now loop through digits and add them to the result
  for(int j=0; j < i+1; j++){
    result_addition = num[j]*pow(10, (i-j));
    // check if the result is too big
    if(result + result_addition >= INT_MAX){
      return 0;
    }
    result = result + result_addition;
  }
  //we took the sign info at the beginning, now we tag it back on
  return result * sign;

};
