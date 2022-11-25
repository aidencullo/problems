package LLMerge;

public class TestCase {

    int [][] input;
    int [] answer;

    public TestCase(String raw){
	String [] strInput = raw.split(" ");
	input = stringToDoubleArray(strInput[0]);
	answer = stringToDoubleArray(strInput[1]);

    }

    private int [][] stringToArrayArray(String str){
	return new int [1][];
    }
    
    private int [] stringToArray(String str){
	return new int [1];
    }

    private String arrayToString(int [] array){
	return "";
    }

    protected void success(){
	System.out.println("Success!");
    }

    protected void fail(){
	System.out.println("Fail");
    }
    
}	
