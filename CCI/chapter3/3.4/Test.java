public class Test{

    Node head;

    public Test(){
	head = new Node(0);
    }
    
    public class Node{

	int val;
	Node next;

	public Node(int v){

	    val = v;

	}
    }

    public void addNode(){

	Node n = new Node(1);
	n.next = head;
	head = n;

    }

    public void print(){

	Node tmp = new Node(0);
	tmp = head;
	while(tmp != null){

	    System.out.println(tmp.val);
	    tmp = tmp.next;
	}
    }

    public static void main(String[] args){

	Test test = new Test();
	test.addNode();
	test.print();
	Node n;

    }
}
