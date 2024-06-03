class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        cipher = {}
        key_without_spaces = key.replace(' ', '')
        key_without_duplicates = ''.join(dict.fromkeys(key_without_spaces))
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        cipher = {
            key: letter
            for key, letter in zip(key_without_duplicates, alphabet)
        }
        message_list = list(message)
        for i, letter in enumerate(message_list):
            if letter.isalpha():
                message_list[i] = cipher[letter]
        return ''.join(message_list)
