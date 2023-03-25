#code from chatgpt
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, data):
        if self.is_empty():
            return
        elif self.head == self.tail and self.head.data == data:
            self.head = None
            self.tail = None
        else:
            curr_node = self.head
            prev_node = None
            while curr_node != self.tail:
                if curr_node.data == data:
                    if prev_node:
                        prev_node.next = curr_node.next
                    else:
                        self.head = curr_node.next
                    return
                prev_node = curr_node
                curr_node = curr_node.next
            if curr_node.data == data:
                prev_node.next = self.head
                self.tail = prev_node
def main():
    # create a circular linked list
    cll = CircularLinkedList()

    # add some nodes to the list
    cll.add(1)
    cll.add(2)
    cll.add(3)
    cll.add(4)

    # print the list
    print("List after adding nodes:")
    print_list(cll)

    # remove a node from the list
    cll.remove(3)

    # print the list
    print("List after removing node with data 3:")
    print_list(cll)

    # remove another node from the list
    cll.remove(1)

    # print the list
    print("List after removing node with data 1:")
    print_list(cll)

def print_list(cll):
    if cll.is_empty():
        print("The list is empty.")
    else:
        curr_node = cll.head
        while curr_node != cll.tail:
            print(curr_node.data, end=" -> ")
            curr_node = curr_node.next
        print(curr_node.data, end=" -> ")
        print(cll.head.data)

if __name__ == "__main__":
    main()
