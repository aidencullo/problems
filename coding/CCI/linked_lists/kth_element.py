
class Node:
    
    def __init__(self, input):
        self.val = input
        self.next = None

def pop_list(array):
    head = None
    for x in reversed(array):
        head = add_node(x, head)
    return head

def add_node(val, head):
    nuevo = Node(val)
    nuevo.next = head
    head = nuevo
    return head

def return_k(head,k):
    if head == None:
        return 0
    index = return_k(head.next, k) + 1
    if index == k:
        print("Value at index %d from the end is %d" % (k, head.val))
    return index

def print_list(head):
    if head == None:
        print("None head node passed")
        return
    print("printing list...")
    node = head
    while(node != None):
        print(node.val)
        node = node.next


input = [1,2,3,4,5]
input_k = 2
list = pop_list(input)
print_list(list)

print("Should print: ", input_k)
print(return_k(list, input_k))
 
input = [1,2,3,4,5]
input_k = 1
list = pop_list(input)
print_list(list)

print("Should print: ", input_k)
print(return_k(list, input_k))
