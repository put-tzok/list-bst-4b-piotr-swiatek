from linked_list.Node import Node


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def find(self, key):
        current_node = self.head

        while current_node is not None:
            if current_node.data == key:
                return current_node
            current_node = current_node.next

