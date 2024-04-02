package LLMerge;

class Algorithm {

    protected ListNode mergeAll(ListNode [] input){
	if(input.length == 0){
	    return null;
	}
	ListNode merged = input[0];
	for(int i = 1; i < input.length; i++){
	    merged = merge(merged, input[i]);
	}
	return merged;
    }

    protected ListNode merge(ListNode base, ListNode extra){
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
	    base = ifNext(base);
	} else {
	    merged = extra;
	    extra = ifNext(extra);
	}

	// we keep track of front to return the merged list later
	ListNode start = merged;
	
	while(base != null && extra != null){
	    // now we just add the smallest next element in base or extra and increment on the list where we took the value
	    if(base.val <= extra.val){
		merged.next = base;
		merged = ifNext(merged);
		base = ifNext(base);
	    } else {
		merged.next = extra;
		merged = ifNext(merged);
		extra = ifNext(extra);
	    }
	}

	// there could be more elements en either the base or extra list (but not both)
	if(base != null){
	    merged.next = base;
	} else if(extra != null){
	    merged.next = extra;
	}
	
	return start;
    }

    private ListNode ifNext(ListNode ln){
	if(ln.next == null){
	    return null;
	}
	return ln.next;
    }
}
