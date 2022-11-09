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
	int [][] inputs = stringToArray(input);
	// expected combined linked lisk
	int [] output = stringToArray(expected);
	for(int i = 0; i < inputs.size(); i++){
	    test(inputs[i]);
	}
    }
    
    private void test(int[] intArray){}
}
