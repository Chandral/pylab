class Node(object):
    def __init__(self, data, node=None):
        self.data = data
        self.next_node = node

    def get_next(self):
        return self.next_node

    def set_next(self, node):
        self.next_node = node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data


class LinkedList(object):
    def __init__(self, root_node=None):
        self.root_node = root_node
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, data):
        new_node = Node(data, self.root_node)
        self.root_node = new_node
        self.size += 1

    def remove(self, data):
        this_node = self.root_node
        prev_node = None
        while this_node is not None:
            if this_node.get_data() == data:
                pass
            else:
                pass

    def find(self):
        pass


def main():
    pass


main()
