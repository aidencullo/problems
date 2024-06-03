class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        letter_key = 'a'
        cipher = {}
        for letter in key:
            if letter.isalpha() and letter not in cipher:
                cipher[letter] = letter_key
                letter_key = chr(ord(letter_key) + 1)
        message_list = list(message)
        for i, letter in enumerate(message_list):
            if letter.isalpha():
                message_list[i] = cipher[letter]
        return ''.join(message_list)
