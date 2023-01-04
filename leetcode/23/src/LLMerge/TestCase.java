package LLMerge;

public class TestCase {

    int [][] input;
    int [] answer;
    String inputString;
    String answerString;
    ListNode answerList;
    ListNode [] inputListOfLists;
    ListNode outputList;

    public TestCase(String raw){
	String [] strInput = raw.split(" ");
	inputString = strInput[0];
	answerString = strInput[1];
	input = stringToDoubleArray(strInput[0]);
	answer = stringToArray(strInput[1]);
	answerList = arrayToList(answer);
	inputListOfLists = arrayToListOfLists(input);
	System.out.println("Creating TestCase object" + inputString);
    }

    protected int [][] stringToDoubleArray(String str){
	String[] singleArrays = str.substring(1, str.length()-2).split(",");
	int [][] arrayOfArrays = new int [singleArrays.length][];
	for(int i = 0; i < arrayOfArrays.length; i++){
	    arrayOfArrays[i] = stringToArray(singleArrays[i]);
	}
	return arrayOfArrays;
    }
    
    protected int [] stringToArray(String str){
	String[] stringArray = str.replaceAll("\\[", "").replaceAll("]", "").split(",");
	int [] arrayOfInts = new int [stringArray.length];
	for(int i = 0; i < arrayOfInts.length; i++){
	    arrayOfInts[i] = Integer.parseInt(stringArray[i]);
	}
	return arrayOfInts;
    }

    protected void success(){
	System.out.println("Success!");
    }

    protected void fail(){
	System.out.println("Fail");
	printList(outputList);
	printList(answerList);
    }

    protected void print(){
	System.out.println("Input: " + inputString + " Expected Output: " + answerString);
    }

    protected void printArray(int [] array){
	for(int i = 0; i < array.length; i++){
	    System.out.println(array[i]);
	}
    }

    protected void printList(ListNode list){
	while(list != null){
	    System.out.print(list.val + " -> ");
	    list = list.next;
	}
	System.out.println();
    }

    protected void printDoubleArray(int [][] doubleArray){
	for(int i = 0; i < doubleArray.length; i++){
	    printArray(doubleArray[i]);
	}
    }

    protected ListNode [] arrayToListOfLists(int [][] array){
	ListNode [] listOfLists = new ListNode [array.length];
	for(int i = 0; i < array.length; i++){
	    listOfLists[i] = arrayToList(array[i]);
	}
	return listOfLists;
    }

    protected ListNode arrayToList(int [] array){
	ListNode node = new ListNode(array[array.length-1]);
	for(int i = array.length-2; i >= 0; i--){
	    node = new ListNode(array[i], node);
	}
	return node;
    }

}	
