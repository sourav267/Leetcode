class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count = 0
        for sentence in sentences:
            if count < len(sentence.split(' ')):
                count = len(sentence.split(' '))
        return count
        