/**
* Class Name: TESTSUITE
* TestSuite runs tests on my main solution algorithm 
* To do:
*     - Implement test function
*     - Implement string to array conversion functions
* 
*/

package testpkg;

import solpkg.Solution;

class TestSuite {
    
    private void run(String input, String expected){
	// converting input into an array of ListNodes
	int [][] inputs = stringToArrayArray(input);
	// expected combined linked lisk
	int [] output = stringToArray(expected);
	for(int i = 0; i < inputs.length; i++){
	    test(inputs[i]);
	}
    }
    
    private void test(int[] intArray){}
    private int [][] stringToArrayArray(String str){
	return new int [1][];
    }
    private int [] stringtoArray(String str){
	return new int [1];
    }
}
