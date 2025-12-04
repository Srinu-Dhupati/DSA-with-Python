class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i not in ["+","-","*","/"]:
                stack.append(int(i))
            else:
                top=stack.pop()
                pre_top=stack.pop()
                if i == "+":
                    stack.append(top+pre_top)
                elif i=="-":
                    stack.append(pre_top-top)
                elif i=="*":
                    stack.append(top*pre_top)
                else:
                    stack.append(int(pre_top/top))
        return stack[0]