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

    protected ListNode run(ListNode [] input){
	Algorithm alg = new Algorithm();
	return alg.mergeAll(input);
    }

    protected void runTest(TestCase tc){
	tc.print();
	tc.outputList = run(tc.inputListOfLists);
	if(compare(tc.outputList, tc.answerList)){
	    tc.success();
	} else {
	    tc.fail();
	}	
    }

    protected boolean compare(ListNode l1, ListNode l2){
	while(l1 != null){
	    if(l2 == null)
		return false;
	    if(l1.val != l2.val)
		return false;
	    l1 = l1.next;
	    l2 = l2.next;
	}
	if(l2 != null)
	    return false;
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
