public class QueueFromStack {


    public class Stack{

	Node head;

	public Stack(){

	    head = null;

	}

	public int pop() {

	    int retval = -1;

	    if(head == null){
		System.out.println("Illegal pop(), no hay elementos");

	    } else {

		retval = head.val;
		head = head.next;
		return retval;
	    }


	    return retval;
	}

	public void push(int val){

	    Node n = new Node(val);
	    n.next = head;
	    head = n;

	}

	public int peek(){

	    int retval = -1;
	    
	    if(head == null){
		
		System.out.println("Illegal peek(), no hay elementos");
		retval = -1;
	    } else {

		retval = head.val;
 	    
	    }
	    return retval;
	}

	public boolean isEmpty(){

	    return head == null;

	}

    }
    
    public class Node{

	int val = -1;
	Node next = null;

	public Node(int newval){
	    val = newval;

	}

    }

    Stack Helper;
    Stack Main;	

    public QueueFromStack(){

	Helper = new Stack();
	Main = new Stack();

    }
    
    public void transferToHelper(){

	while(!Main.isEmpty()){

	    Helper.push(Main.pop());

	}

    }

    public void transferToMain(){

	while(!Helper.isEmpty()){

	    Main.push(Helper.pop());

	}

    }

	
    public int pop(){

	return Main.pop();
	
    }

    public void push(int val){

	transferToHelper();
	Main.push(val);
	transferToMain();
	
    }

    public int peek(){

	return Main.peek();

    }

    public boolean isEmpty(){

	return Main.isEmpty();

    }

    public void popAll(){

	while(!Main.isEmpty()){
	    pop();

	}

    }


    public static void main(String[] args){

	QueueFromStack qfs = new QueueFromStack();
	qfs.push(1);
	qfs.push(2);
	qfs.push(3);
	qfs.push(4);
	System.out.println("1 == " + qfs.peek());
	System.out.println("false == " + qfs.isEmpty());
	qfs.pop();
	System.out.println("2 == " + qfs.peek());
	qfs.pop();
	qfs.pop();
	System.out.println("4 == " + qfs.peek());
	qfs.push(100);
	qfs.pop();
	System.out.println("100 == " + qfs.peek());
	qfs.popAll();
	System.out.println(qfs.peek());
	System.out.println("true == " + qfs.isEmpty());

    }
    
}
