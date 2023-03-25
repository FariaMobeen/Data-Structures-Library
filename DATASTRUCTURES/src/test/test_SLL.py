import sys
sys.path.append('/path/to/main/package')
from main.python.mylib.datastructures.linear.SLL import LinkedList

def test_insert_at_head():
    linked_list = LinkedList()
    linked_list.insert_at_head(1)
    linked_list.insert_at_head(2)
    linked_list.insert_at_head(3)
    assert linked_list.head.data == 3

def test_insert_at_tail():
    linked_list = LinkedList()
    linked_list.insert_at_tail(1)
    linked_list.insert_at_tail(2)
    linked_list.insert_at_tail(3)
    assert linked_list.head.data == 1
    assert linked_list.head.next.data == 2
    assert linked_list.head.next.next.data == 3

def test_search():
    linked_list = LinkedList()
    linked_list.insert_at_head(1)
    linked_list.insert_at_head(2)
    linked_list.insert_at_head(3)
    assert linked_list.search(2) == True
    assert linked_list.search(4) == False

def test_delete_at_head():
    linked_list = LinkedList()
    linked_list.insert_at_head(1)
    linked_list.insert_at_head(2)
    linked_list.insert_at_head(3)
    assert linked_list.delete_at_head() == 3
    assert linked_list.head.data == 2

def test_delete_at_tail():
    linked_list = LinkedList()
    linked_list.insert_at_head(1)
    linked_list.insert_at_head(2)
    linked_list.insert_at_head(3)
    assert linked_list.delete_at_tail() == 1
    assert linked_list.head.next.next == None
