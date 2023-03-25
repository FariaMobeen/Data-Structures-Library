#code from chatgpt
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items[0]

    def size(self):
        return len(self.items)
def main():
    # create a new queue
    q = Queue()

    # enqueue some items
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    # print the queue
    print("Queue after enqueuing 3 items:")
    print(q.items)

    # dequeue an item
    item = q.dequeue()
    print(f"Dequeued item: {item}")

    # print the queue
    print("Queue after dequeuing an item:")
    print(q.items)

    # peek at the front of the queue
    front_item = q.peek()
    print(f"Front item: {front_item}")

    # print the queue size
    print(f"Queue size: {q.size()}")

if __name__ == "__main__":
    main()
