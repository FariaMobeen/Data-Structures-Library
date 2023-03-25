#code from chatgpt
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
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
            new_node.prev = new_node
            new_node.next = new_node
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.head.prev = new_node
            self.tail.next = new_node
            self.tail = new_node
    
    def remove(self, data):
        if self.is_empty():
            return False
        curr_node = self.head
        while curr_node.data != data:
            curr_node = curr_node.next
            if curr_node == self.head:
                return False
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif curr_node == self.head:
            self.head = curr_node.next
            self.tail.next = self.head
            self.head.prev = self.tail
        elif curr_node == self.tail:
            self.tail = curr_node.prev
            self.head.prev = self.tail
            self.tail.next = self.head
        else:
            curr_node.prev.next = curr_node.next
            curr_node.next.prev = curr_node.prev
        return True
def main():
    # create a circular doubly linked list
    cdll = CircularDoublyLinkedList()

    # add some nodes to the list
    cdll.add(1)
    cdll.add(2)
    cdll.add(3)
    cdll.add(4)

    # print the list
    print("List after adding nodes:")
    print_list(cdll)

    # remove a node from the list
    cdll.remove(3)

    # print the list
    print("List after removing node with data 3:")
    print_list(cdll)

    # remove another node from the list
    cdll.remove(1)

    # print the list
    print("List after removing node with data 1:")
    print_list(cdll)

def print_list(cdll):
    if cdll.is_empty():
        print("The list is empty.")
    else:
        curr_node = cdll.head
        while True:
            print(curr_node.data, end=" <-> ")
            curr_node = curr_node.next
            if curr_node == cdll.head:
                break
        print()

if __name__ == "__main__":
    main()
