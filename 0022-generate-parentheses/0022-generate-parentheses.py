class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def add_parenthesis(string, left, right):
            if left == 0 and right == 0:
                result.append(string)
            if left > 0:
                add_parenthesis(string + '(', left-1, right)
            if right > 0 and right > left:
                add_parenthesis(string + ')', left, right-1)
        result = []
        add_parenthesis('',n,n)
        return result
        