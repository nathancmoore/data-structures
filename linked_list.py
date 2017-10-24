"""Form a linked list using classes."""


class Node(object):
    """Define Node-class objects."""

    def __init__(self, data=None, next=None):
        """Initiate a new instance of a Node object with attributes."""
        self.data = data
        self.next = next


class LinkedList(object):
    """Define LinkedList-class objects."""

    def __len__(self):
        """Change the len() method."""
        return self.size()

    def __str__(self):
        """Change the print() method."""
        return self.display()

    def __init__(self):
        """Initiate a new instance of a LinkedList object with attributes."""
        self.head = None

    def size(self):
        """Define the size method of the LinkedList-class object."""
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def push(self, val):
        """Define the push method for LinkedList-class object."""
        new_node = Node(val, self.head)
        self.head = new_node

    def search(self, val):
        """Search the linked list for a node with a particular value."""
        current_node = self.head
        while current_node:
            if current_node.data == val:
                return current_node
            current_node = current_node.next
        return None

    def remove(self, val):
        """Remove a node from the list."""
        previous_node = None
        current_node = self.head
        while current_node:
            if current_node.data == val:
                if previous_node:
                    previous_node.next = current_node.next
                    return None
                else:
                    self.head = current_node.next
                    return None
            previous_node = current_node
            current_node = current_node.next
        raise ValueError("Data not in list")

    def pop(self):
        """Remove and returns the head node of the list."""
        if self.head is None:
            raise IndexError("List is empty")
        else:
            popped_node = self.head
            self.head = self.head.next
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
