max_size = 5
stack = [ ]
top = -1
def push (book_title):
    global top
    if top >= max_size-1:
        print("stack over flow cannot push more book")
    else:
        top+=1
        stack.append(book_title)
        print(f"book:{book_title}pushed on the stack")
def pop ():
    global top
    if top ==-1:
        print("stack under flow cannot print any book")
    else:
        remove_book = stack.pop()
        print (f"book.{remove_book}popped from the stack")
        top -= 1
def peek ():
    if top == -1:
        print("stack is empty")
    else:
        print(f"top book on the stack{stack[top]}")
def display():
    if top == -1:
        print("stack is empty:")
    else:
        print("book in the stack (top to bottom):")
        for i in range (top,-1,-1):
            print(f"{[i+1],stack[i]}")
push("abc")
push("def")
push("ghi")
pop()
peek()
display()
        
        
        
