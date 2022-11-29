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
	String[] singleArrays = str.substring(1, str.length()-2).split(",");
	int [][] arrayOfArrays = new int [singleArrays.length][];
	for(int i = 0; i < arrayOfArrays.length; i++){
	    arrayOfArrays[i] = stringToArray(singleArrays[i]);
	}
    }
    
    protected int [] stringToArray(String str){
	String[] stringArray = str.replaceAll("\\[", "").replaceAll("]", "").split(",");
	int [] arrayOfInts = new int [stringArray.length];
	for(int i = 0; i < arrayOfInts.length; i++){
	    arrayOfInts[i] = \\parseint
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

    protected void printArray(int [] array){
	for(int i = 0; i < array.length; i++){
	    System.out.println(array[i]);
	}
    }

    protected void printDoubleArray(int [][] doubleArray){
	for(int i = 0; i < doubleArray.length; i++){
	    printArray(doubleArray[i]);
	}
    }

}	
