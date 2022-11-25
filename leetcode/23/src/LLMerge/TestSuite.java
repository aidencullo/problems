/*
* Class Name: TESTSUITE
* TestSuite runs tests on my main solution algorithm 
* To do:
*     - Implement test function
*     - Implement string to array conversion functions
* 
*/

package LLMerge;

import java.util.ArrayList;
import java.util.Iterator;

public class TestSuite {

    private String testFile;
    ArrayList<TestCase> tests;
    
    
    public TestSuite(String fileName){
	testFile = fileName;
	tests= new ArrayList<TestCase>();
    }

    private String run(int [][] input){
	return "";
    }

    private void runTest(TestCase ts){

	ts.print();
	int [] outputArray = run(ts.input);
	String outputString = ts.arrayToString(outputArray);
	if(outputString == ts.answer){
	    ts.fail();
	} else {
	    ts.succeed();
	}		
	
    }

    public void runTests(){

	initialize();
	for(Iterator<TestCase> iter = list.iterator(); iter.hasNext(); iter++){
	    runTest(iter.next());
	}

    }

    private void readFile(){

	// checking that test file was provided
	if(testFile == ""){
	    System.out.println("No test file provided");
	    return;
	}
	//reading test input, inputs variable should be string array of size 2
	String input;
	try  {
	    input = ReadFile.read(testFile);
	} catch(Exception e) {
	    System.out.println("File not read properly");
	}
    }

    private void initialize(){

	readFile();
	setTestCases();
	
    }
        
}
