class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        n = len(word)

        if n < 3:
            return False
        is_valid = False

        vowels = set('aeiouAEIOU')

        for w in word:
            if not w.isalnum():
                return False
            else:
                if w in vowels:
                    is_valid = True
        return is_valid