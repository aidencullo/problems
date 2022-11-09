package solpkg

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
	largeList = ListNode();
	for(int i = 0; i < lists.size(); i++){
	    mergeLists(largeList, lists[i])
	}
	return largeList;
    }
}
