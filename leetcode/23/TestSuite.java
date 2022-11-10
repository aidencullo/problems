/**
* Class Name: TESTSUITE
* TestSuite runs tests on my main solution algorithm 
* To do:
*     - Implement test function
*     - Implement string to array conversion functions
* 
*/

package testpkg;

import scanpkg.ReadFile;
import solpkg.Solution;

class TestSuite {

    private String testFile;
    
    public TestSuite(String fileName){
	testFile = fileName;
    }
    
    private void initialize(){
	// checking that test file was provided
	if(testFile == ""){
	    System.out.println("No test file provided");
	    return;
	}
	//reading test input, inputs variable should be string array of size 2
	String [] inputs = new [2] String;
	inputs = ReadFile(testFile);
	// test input
	run(input[0], input[1]);
    }
    
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
