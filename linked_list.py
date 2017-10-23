"""This is the docstring."""


class Node(object):
    """Define Node-class objects."""

    def __init__(self, data=None, next=None):
        """Initiate a new instance of a Node object with attributes."""
        self.data = data
        self.next = next

    def get_data(self):
        """Write something here."""
        return self.data

    def set_data(self, data):
        """Write something here."""
        self.data = data

    def set_next(self, next):
        """Define what the next node is."""
        self.next = next

    def get_next(self):
        """Return what the next node is."""
        return self.next


class LinkedList(object):
    """Define LinkedList-class objects."""

    def __init__(self):
        """Initiate a new instance of a LinkedList object with attributes."""
        self.head = None

    def size(self):
        """Define the size method of the LinkedList-class object."""
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.get_next()
        return count

    def push(self, val):
        """Define the push method for LinkedList-class object."""
        new_node = Node(val, self.head)
        self.head = new_node

    def search(self, val):
        """Search the linked list for a node with a particular value."""
        current_node = self.head
        while current_node:
            if current_node.get_data() == val:
                return current_node
            current_node = current_node.get_next()
        return None

    def remove(self, val):
        """Remove a node from the list."""
        previous_node = None
        current_node = self.head
        while current_node:
            if current_node.get_data() == val:
                if previous_node:
                    previous_node.next = current_node.get_next()
                    return None
                else:
                    self.head = current_node.get_next()
                    return None
            previous_node = current_node
            current_node = current_node.get_next()
        raise ValueError("Data not in list")
