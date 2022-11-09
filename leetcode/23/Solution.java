package solpkg

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
	largeList = ListNode();
	for(int i = 0; i < lists.size(); i++){
	    mergeLists(largeList, lists[i])
	}
	return largeList;
    }
}
