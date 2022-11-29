ackage LLMerge;

import java.util.ArrayList;
import java.util.Iterator;

public class TestSuite {

    private String testFile;
    ArrayList<TestCase> tests;
    
    
    public TestSuite(String fileName){
	testFile = fileName;
	tests= new ArrayList<TestCase>();
    }

    protected int[] run(int [][] input){
	Algorithm alg = new Algorithm();
	alg.mergeAll(input);
	return new int []{1};
    }

    protected void runTest(TestCase tc){

	tc.print();
	if(compare(run(tc.input), tc.answer)){
	    tc.fail();
	} else {
	    tc.success();
	}		
	
    }

    protected boolean compare(int [] array1, int [] array2){
	if(array1.length != array2.length){
	    return false;
	}
	for(int i = 0; i < array1.length; i++){
	    if(array1[i] != array2[i]){
		return false;
	    }
	}
	return true;
    }	    

    public void runTests(){

	initialize();
	Iterator<TestCase> iter = tests.iterator();
	while(iter.hasNext()){
	    runTest(iter.next());
	}

    }

    protected ArrayList<String> readFile(){

	// checking that test file was provided
	if(testFile == ""){
	    System.out.println("No test file provided");
	}
	//reading test input, inputs variable should be string array of size 2
	ArrayList<String> inputStrings = new ArrayList<String>();
	try  {
	    inputStrings = ReadFile.read(testFile);
	} catch(Exception e) {
	    System.out.println("File not read properly");
	}
	return inputStrings;
    }

    protected void initialize(){
	setTestCases(readFile());
    }

    protected void setTestCases(ArrayList<String> strs){
	for(int i = 0; i < strs.size(); i++){
	    tests.add(new TestCase(strs.get(i)));
	}
    }
}
