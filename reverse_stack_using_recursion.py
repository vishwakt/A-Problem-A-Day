def reverse(stack):
    if not isEmpty(stack):
        temp = pop(stack)
        reverse(stack)
        push(stack, temp)
        pass


def insertAtBottom(stack, item):
    if isEmpty(stack):
        push(stack, item)
    else:
        temp = pop(stack)
        insertAtBottom(stack, item)
        push(stack, temp)


def isEmpty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)


def pop(stack):
    if isEmpty(stack):
        print "Stack Underflow"
        exit(1)
    return stack.pop()


def printStack(stack):
    for i in range(len(stack)-1, -1, -1):
        print stack[i], ' '
    print


stack = []
push(stack, str(4))
push(stack, str(3))
push(stack, str(2))
push(stack, str(1))
print("Original Stack ")
printStack(stack)

reverse(stack)

print("Reversed Stack ")
printStack(stack)