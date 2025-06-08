class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        temp = []
        for i in range(len(words)):
            if x in words[i]:
                temp.append(i)
        
        return temp
        