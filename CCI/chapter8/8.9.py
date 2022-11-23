 def parens(n):
        if n == 1:
                return ["()"]
        else:
                a = parens(n-1)
                b = ["(" + x + ")" for x in a]
                c = ["()" + x for x in a]
                d = [x + "()" for x in a]
                return set(b+c+d)

                
print(parens(4))
