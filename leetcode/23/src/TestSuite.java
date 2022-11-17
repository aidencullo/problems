/**
* Class Name: TESTSUITE
* TestSuite runs tests on my main solution algorithm 
* To do:
*     - Implement test function
*     - Implement string to array conversion functions
* 
*/

package LLMerge;

public class TestSuite {

    private String testFile;
    
    public TestSuite(String fileName){
	testFile = fileName;
    }


    private int [][] stringToArrayArray(String str){
	return new int [1][];
    }
    
    private int [] stringToArray(String str){
	return new int [1];
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
    
    private void initialize(){
	// checking that test file was provided
	if(testFile == ""){
	    System.out.println("No test file provided");
	    return;
	}
	//reading test input, inputs variable should be string array of size 2
	String [] inputs = new String [2];
	try  {
	    ReadFile.read(testFile);
	} catch(Exception e) {
	    System.out.println("File not read properly");
	}
	//	inputs = ReadFile.read(testFile);
	// test input
	run("", "");
    }
    
    
    private void test(int[] intArray){}
    
}
