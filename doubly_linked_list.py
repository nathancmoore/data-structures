"""Define the class of DLinkedList."""


class Node(object):
    """Define Node-class objects."""

    def __init__(self, data, next_node=None, prev_node=None):
        """Initiate a new instance of a Node object with attributes."""
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class DLinkedList(object):
    """Define the class of DLinkedList."""

    def __len__(self):
        """Change the len() method."""
        return self.size()

    def __str__(self):
        """Change the print() method."""
        return self.display()

    def __init__(self):
        """Initiate a new instance of a DLinkedList object with attributes."""
        self.head = None
        self.tail = None

    def size(self):
        """Define the size method of the DLinkedList-class object."""
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            if current_node.next_node:
                current_node = current_node.next_node

            else:
                break

        return count

    def push(self, val):
        """Define the push method for DLinkedList-class object."""
        new_node = Node(val)

        if self.size() == 0:
            self.tail = new_node
            self.head = new_node

        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node

        self.head = new_node

    def append(self, val):
        """Define the append method for DLinkedList-class object."""
        new_node = Node(val)

        if self.size() == 0:
            self.tail = new_node
            self.head = new_node

        else:
            new_node.prev_node = self.tail
            self.tail.next_node = new_node

        self.tail = new_node

    def search(self, val):
        """Search the linked list for a node with a particular value."""
        current_node = self.head

        while current_node:

            if current_node.data == val:
                return current_node

            current_node = current_node.next_node

        return None

    def remove(self, val):
        """Remove a node from the list."""
        current_node = self.head

        while current_node:

            if current_node.data == val:

                if current_node == self.head:
                    self.head = current_node.next_node
                    self.head.prev_node = None
                    return

                elif current_node == self.tail:
                    self.tail = current_node.prev_node
                    self.tail.next_node = None
                    return

                else:
                    current_node.prev_node.next_node = current_node.next_node
                    current_node.next_node.prev_node = current_node.prev_node
                    return

            else:
                current_node = current_node.next_node

        raise ValueError("Data not in list")

    def pop(self):
        """Remove and returns the head node of the list."""
        if self.head is None:
            raise IndexError("List is empty")

        else:
            popped_node = self.head
            self.head = self.head.next_node
            return popped_node.data

    def display(self):
        """Display unicode string of linked list contents."""
        display_str = "("

        if self.head is None:
            return "()"

        current_node = self.head

        while current_node:

            if current_node.next is None:
                display_str += str(current_node.data) + ")"
                return display_str

            else:
                display_str += str(current_node.data) + ", "
                current_node = current_node.next

    def shift(self):
        """Remove and return the tail node of the list."""
        if self.tail is None:
            raise IndexError("List is empty")

        else:
            shift_node = self.tail
            self.tail = self.tail.prev_node
            return shift_node.data
