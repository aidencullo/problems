package LLMerge;

public class TestCase {

    int [][] input;
    int [] answer;
    String inputStr;
    String outputStr;

    public TestCase(String raw){
	String [] strInput = raw.split(" ");
	inputStr = strInput[0];
	outputStr = strInput[1];
	input = stringToDoubleArray(strInput[0]);
	answer = stringToArray(strInput[1]);

    }

    protected int [][] stringToDoubleArray(String str){
	return new int [1][];
    }
    
    protected int [] stringToArray(String str){
	return new int [1];
    }

    protected String arrayToString(int [] array){
	return "";
    }

    protected void success(){
	System.out.println("Success!");
    }

    protected void fail(){
	System.out.println("Fail");
    }


    protected void print(){
	System.out.println("Input: " + inputStr + " Expected Output: " + outputStr);
    }
}	
