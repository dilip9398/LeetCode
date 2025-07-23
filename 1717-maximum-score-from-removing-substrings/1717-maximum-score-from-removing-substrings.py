class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        
        def remove_pair(s, first, second, gain):
            stack = []
            score = 0
            for c in s:
                if stack and stack[-1] == first and c == second:
                    stack.pop()
                    score += gain
                else:
                    stack.append(c)
            return ''.join(stack), score  # Return updated string and score
        
        total_score = 0

        # Step 1: remove higher value pair first
        if x >= y:
            # Remove "ab" first
            s, pts = remove_pair(s, 'a', 'b', x)
            total_score += pts
            # Then try removing "ba"
            s, pts = remove_pair(s, 'b', 'a', y)
            total_score += pts
        else:
            # Remove "ba" first
            s, pts = remove_pair(s, 'b', 'a', y)
            total_score += pts
            # Then remove "ab"
            s, pts = remove_pair(s, 'a', 'b', x)
            total_score += pts

        return total_score
