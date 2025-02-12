class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        transformations = set()
        for word in words:
            transformation = []
            for letter in word:
                transformation.append(morse[alphabet.index(letter)])
            transformations.add(''.join(transformation))
        return len(transformations)
