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

    def remove(self, key):
        current_node = self.head

        if current_node is not None:
            if current_node.data == key:
                self.head = current_node.next
                return

        while current_node is not None:
            if current_node.data == key:
                break
            prev = current_node
            current_node = current_node.next

        if current_node is None:
            return

        prev.next = current_node.next

    def get_node(self, key):
        current_node = self.head

        while current_node is not None:
            if current_node.data == key:
                return current_node
            current_node = current_node.next

    def display(self):
        elements = []
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)

