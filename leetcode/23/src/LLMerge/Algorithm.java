package LLMerge;

class Algorithm {

    protected int[] mergeAll(int [][] input){
	int size = 0;
	for(int i = 0; i < input.length; i++)
	    size += input[i].length;
	int [] output = new int [size];
	for(int i = 0, k = 0; i < output.length; i++){
	    k += input[i];
	    merge(output, input[i], k);
	}
	return output;
    }

    protected void merge(int [] base, int [] adder, int bound){
	for(int i = 0; i < bound; i++){
	    if(base[i] < adder[i]){
		
    }
}
