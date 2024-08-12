def solution(src):
    stack = []
    for char in src:
        if len(stack) > 1 and stack[-1] == "_" and stack[-2] != "_" and stack[-2]!= " " and char != "_" and char != " ":
            stack.pop()
            stack.append(char.upper())
        else:
            stack.append(char)
    res = ''.join(stack)
    return res

assert solution("qvgtNTn gHEnbVu _sriel_ cjk_m uu") == "qvgtNTn gHEnbVu _sriel_ cjkM uu"

assert solution("the_variable") == "theVariable"
assert solution("the_variable__") == "theVariable__"
assert solution("_the_variable") == "_theVariable"
assert solution("_the_variable__") == "_theVariable__"
assert solution("This is the doc_string for __secret_fun") == "This is the docString for __secretFun"

