from heap import MinHeap


def process_instruction(instr: str):
    instr = instr.split()
    if len(instr) == 2:
        data = instr[1]
        if instr[0] == '1':
            numbers.insert(data)
        else:
            numbers.delete(data)
    else:
        print(numbers.get_min())
            
def process_input(q: int=5):
    for i in range(q):
        process_instruction(input())

numbers = MinHeap()
q = int(input())
process_input(q)
