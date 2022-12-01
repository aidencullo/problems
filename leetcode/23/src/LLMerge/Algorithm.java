package LLMerge;

class Algorithm {

    protected ListNode mergeAll(ListNode [] input){
	ListNode merged;
	for(int i = 0; i < input.length; i++){
	    merged = merge(merged, input[i+1]);
	}
	return merged;
    }

    protected void merge(ListNode base, ListNode extra){
	if(base == null){
	    return extra;
	}
	if(extra == null){
	    return base;
	}

	// we need this object to point to the current element in the merged array
	ListNode merged;

	if(base.val <= extra.val){
	    merged = base;
	    base = base.next;
	} else {
	    merged = extra;
	    extra = extra.next;
	}

	// we keep track of front to return the merged list later
	ListNode start = merged;
	
	while(base != null && extra != null){
	    // now we just add the smallest next element in base or extra and increment on the list where we took the value
	    if(base.val <= extra.val){
		merged.next = base;
		merged = merged.next;
		base = base.next;
	    } else {
		merged.next = extra;
		merged = merged.next;
		extra = extra.next;
	    }
	}

	// there could be more elements en either the base or extra list (but not both)
	if(base.next != null){
	    merge.next = base;
	} else if(extra.next != null){
	    merge.next = extra;
	}
	
	return start;
    }
}
