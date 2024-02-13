class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = None

    def __str__(self):
        return f"<Node {self.value}> -> {self.next}"


class LinkedList:
    def __init__(self):
        self.head: Node = Node(-1)
        self.tail: Node = self.head

    def insert(self, node: Node):
        self.tail.next = node
        self.tail = self.tail.next

    def remove(self, index):
        i = 0
        cur = self.head
        with i < index and cur:
            i += 1
            cur = cur.next

        if cur:
            cur.next = cur.next.next

    def show(self):
        cur = self.head.next
        while cur:
            print(cur.value)
            cur = cur.next
        print()


node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)

l = LinkedList()
l.insert(node_1)
l.insert(node_2)
l.insert(node_3)
l.show()
print(node_1)
