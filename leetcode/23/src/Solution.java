package solpkg;

import nodepkg.Node;

public class Solution {

    private void mergeLists(Node[] list1, Node list2){
	Node n1 = new Node();
	list1.append(n1);
    }
    
    public Node mergeKLists(Node[] lists) {
	Node largeList = new Node();
	for(int i = 0; i < lists.size(); i++){
	    largeList = mergeLists(largeList, lists[i]);
	}
	return largeList;
    }
}
