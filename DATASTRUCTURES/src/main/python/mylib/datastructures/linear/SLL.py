#code from chatgpt
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head is None
    
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            
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
        else:
            deleted_node = self.head
            self.head = deleted_node.next
            deleted_node.next = None
            return deleted_node.data
        
    def delete_at_tail(self):
        if self.is_empty():
            return None
        elif self.head.next is None:
            deleted_node = self.head
            self.head = None
            return deleted_node.data
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            deleted_node = current.next
            current.next = None
            return deleted_node.data



# #testing this class implementation
# def main():
#     # create a new linked list
#     linked_list = LinkedList()

#     # add nodes to the list
#     linked_list.insert_at_head(1)
#     linked_list.insert_at_tail(2)
#     linked_list.insert_at_tail(3)
#     linked_list.insert_at_head(0)

#     # check if the list contains a specific value
#     print(linked_list.search(2)) # True
#     print(linked_list.search(4)) # False

#     # remove nodes from the list
#     print(linked_list.delete_at_head()) # 0
#     print(linked_list.delete_at_tail()) # 3

#     # print the remaining nodes in the list
#     current = linked_list.head
#     while current is not None:
#         print(current.data)
#         current = current.next

# if __name__ == '__main__':
#     main()
