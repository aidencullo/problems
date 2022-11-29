package LLMerge;

class Algorithm {

    protected int[] mergeAll(int [][] input){
	int size = 0;
	for(int i = 0; i < input.length; i++)
	    size += input[i].length;
	int [] output = new int [size];
	for(int i = 0; i < output.length; i++){
	    //	    merge(output, input[i]);
	    System.out.println(output[i]);
	}
	return output;
    }

    protected void merge(int [] base, int [] adder){
	//	for(int i = 0; i < adder.length; i++){
	//   if(base[
    }
}
