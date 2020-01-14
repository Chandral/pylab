class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def add_link(self, node):
        try:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = node
        except AttributeError:
            self.head = node

    def insert_link_at(self, node, position):
        try:
            current_node = self.head
            for i in range(1, position):
                current_node = current_node.next
            node.next = current_node

            current_node = self.head
            for i in range(1, position-1):
                current_node = current_node.next
            current_node.next = node
        except AttributeError:
            print("Cannot insert at position {}. Try appending with add_link".format(str(position)))


a = LinkedList()
# [a.add_link(Node(i)) for i in ("a", "b", "c", "d", "e", "f")]
# print(a.head.data)
# print(a.head.next.data)
# print(a.head.next.next.data)
# print(a.head.next.next.next.data)
# print(a.head.next.next.next.next.data)
# print(a.head.next.next.next.next.next.data)
a.insert_link_at(Node(1), 1)
print(a.head.data)
print(a.head.next.data)
print(a.head.next.next.data)
print(a.head.next.next.next.data)
print(a.head.next.next.next.next.data)
print(a.head.next.next.next.next.next.data)