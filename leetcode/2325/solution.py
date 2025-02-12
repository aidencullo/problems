class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        cipher = {}
        key_without_spaces = key.replace(' ', '')
        key_without_duplicates = ''.join(dict.fromkeys(key_without_spaces))
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        cipher = dict(zip(key_without_duplicates, alphabet))
        encrypted_map = map(lambda letter: cipher.get(letter, letter), message)
        return ''.join(encrypted_map)
