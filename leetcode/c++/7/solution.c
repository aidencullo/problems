#include <math.h>
#include <stdio.h>
#include "solution.h"

int execute(int input) {
  int sign=1;
  double num[10]={0};
  int i;
  int result=0;
  int result_addition=0;
  if(input < 0){
    sign = -1;
    input = input*-1;
  }
  for(i=0; i < 10 && input > 0; i++){
    num[i] = input - (input/10)*10;
    input  = input / 10;
  }
  i = i-1;
  for(int j=0; j < i+1; j++){
    result_addition = num[j]*pow(10, (i-j));
    printf("result + result_addition: %d, result: %d\n", result + result_addition, result);
    printf("result + result_addition < result: %d\n", result + result_addition < result);
    if(result + result_addition < result || num[9]>2){
      return 0;
    }
    result = result + result_addition;
  }
  return result * sign;
};
