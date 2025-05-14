class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {}
        letter = 0
        key = "".join(key.split())
        for c in key:  
            if c not in d:        
                new_char = chr(97 + letter)
                letter += 1
                d[c] = new_char
            
        res = ""
        for c in message:
            if c == " ":
                res += c
            else:
                res += d[c]
        return res