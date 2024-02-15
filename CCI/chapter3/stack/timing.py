import timeit

from stack import Stack

STEP = 10
ITERATIONS = 10

def time_fn(fn_getter):
    print(f'{fn_getter.__name__}')
    for i in range(1, ITERATIONS):
        n = i * STEP
        t = timeit.timeit(fn_getter(n))
        print(f'{n=}: {t=}, {t/n=}')

def get_push_pop(n):
    def push_pop_n():
        s = Stack()
        for _ in range(n):
            s.push(0)
        for _ in range(n):
            s.pop()
    return push_pop_n


def get_push(n):
    def push_n():
        s = Stack()
        for _ in range(n):
            s.push(0)
    return push_n


def get_peek(n):
    def peek_n():
        s = Stack()
        s.push(0)
        for _ in range(n):
            s.peek()
    return peek_n


def get_is_empty(n):
    def is_empty_n():
        s = Stack()
        s.push(0)
        for _ in range(n):
            s.isEmpty()
    return is_empty_n


time_fn(get_push_pop)
time_fn(get_push)
time_fn(get_peek)
time_fn(get_is_empty)
