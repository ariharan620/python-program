
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def infix_to_postfix(expression):
    stack = []
    postfix = ""
    
    for char in expression:
        if char.isalnum():
            postfix += char
        elif char == '(':
            stack.append(char)
        
       
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()  
        
      
        else:
            while stack and precedence(char) <= precedence(stack[-1]):
              
                if char == '^' and stack[-1] == '^':
                    break
                postfix += stack.pop()
            stack.append(char)

    
    while stack:
        postfix += stack.pop()
    
    return postfix


expr = "a+b*(c^d-e)^(f+g*h)-i"
print("Infix:  ", expr)
print("Postfix:", infix_to_postfix(expr))
