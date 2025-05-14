class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        unique = []
        letter = 0
        key = "".join(key.split())
        for c in key:  
            if c not in unique:
                unique.append(c)
            
        res = ""
        for c in message:
            if c == " ":
                res += c
            else:
                pos = unique.index(c)
                res += chr(97 + pos)
        return res