def parens(n):
    return parenshelp(n,n)

def parenshelp(left, right, str=""):
    if right == 0:
        return [str]
    array=[]
    if left > 0:
        array.extend(parenshelp(left-1, right, str+"("))
    if left < right:
        array.extend(parenshelp(left, right-1, str+")"))
    return array

print(parens(3))
