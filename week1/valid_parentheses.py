class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []
        ind = 0
        parens = "(){}[]"
        for letter in s:
            if parens.index(letter) % 2 == 0:
                stack.append(parens.index(letter))
                ind += 1
            else:
                if len(stack) == 0:
                    return False
                if stack[ind-1] == parens.index(letter) - 1:
                    stack.pop(ind-1)
                    ind -= 1
                else:
                    return False
        return len(stack) == 0
