class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        def get_morse(letter):
            return morse[ord(letter) - 97]
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transformations = set()
        for word in words:
            transformation = []
            for letter in word:
                transformation.append(get_morse(letter))
            transformations.add(''.join(transformation))
        return len(transformations)
