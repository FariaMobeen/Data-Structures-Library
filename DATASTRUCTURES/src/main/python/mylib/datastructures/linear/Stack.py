#code from chatgpt
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise Exception("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise Exception("Stack is empty")

    def size(self):
        return len(self.items)
def main():
    # create a new stack object
    my_stack = Stack()

    # push some items onto the stack
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)

    # print the size of the stack
    print("Size of stack:", my_stack.size())

    # peek at the top item on the stack
    print("Top item on stack:", my_stack.peek())

    # pop an item off the stack
    print("Popped item:", my_stack.pop())

    # print the size of the stack again
    print("Size of stack:", my_stack.size())

    # pop all items off the stack
    while not my_stack.is_empty():
        print("Popped item:", my_stack.pop())

    # try to pop an item off an empty stack
    try:
        my_stack.pop()
    except Exception as e:
        print("Exception caught:", e)
if __name__ == '__main__':
    main()
