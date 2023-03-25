#code from chatgpt
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def delete_at_head(self):
        if self.is_empty():
            return None
        elif self.head == self.tail:
            deleted_node = self.head
            self.head = None
            self.tail = None
            return deleted_node.data
        else:
            deleted_node = self.head
            self.head = deleted_node.next
            self.head.prev = None
            deleted_node.next = None
            return deleted_node.data

    def delete_at_tail(self):
        if self.is_empty():
            return None
        elif self.head == self.tail:
            deleted_node = self.head
            self.head = None
            self.tail = None
            return deleted_node.data
        else:
            deleted_node = self.tail
            self.tail = deleted_node.prev
            self.tail.next = None
            deleted_node.prev = None
            return deleted_node.data


def main():
    # create a new doubly linked list
    dll = DoublyLinkedList()

    # insert some nodes
    dll.insert_at_head(1)
    dll.insert_at_tail(2)
    dll.insert_at_head(3)
    dll.insert_at_tail(4)

    # print the contents of the list
    current = dll.head
    while current is not None:
        print(current.data)
        current = current.next
    # Output: 3 1 2 4

    # search for a node
    print(dll.search(2))  # Output: True
    print(dll.search(5))  # Output: False

    # delete a node
    print(dll.delete_at_head())  # Output: 3
    print(dll.delete_at_tail())  # Output: 4

    # print the contents of the list
    current = dll.head
    while current is not None:
        print(current.data)
        current = current.next
    # Output: 1 2
if __name__ == '__main__':
    main()
