"""Implementation of a binary search tree data structure."""


class Node(object):
    """Define the Node-class object."""

    def __init__(self, value, left=None, right=None, parent=None):
        """Constructor for the Node class."""
        self.val = value
        self.left = left
        self.right = right
        self.parent = parent
        self.depth = 0


class BST(object):
    """Define the BST-class object."""

    def __init__(self, starting_values=None):
        """Constructor for the BST class."""
        self.tree_size = 0
        self.left_depth = 0
        self.right_depth = 0
        self.visited = []
        self.max_depth_reached = 0

        if starting_values is None:
            self.root = None

        elif isinstance(starting_values, (list, str, tuple)):
            self.root = Node(starting_values[0])
            self.tree_size += 1
            for i in range(len(starting_values) - 1):
                self.insert(starting_values[i + 1])

        else:
            raise TypeError('Only iterables or None\
                are valid parameters!')

    def balance(self):
        """Return the current balance of the BST."""
        return self.right_depth - self.left_depth

    def size(self):
        """Return the current size of the BST."""
        return self.tree_size

    def insert(self, value):
        """Insert a new node into the BST, and adjust the balance."""
        new_node = Node(value)

        if self.root:
            if new_node.val > self.root.val:
                if self.root.right:
                    self._find_home(new_node, self.root.right)
                    if new_node.depth > self.right_depth:
                        self.right_depth = new_node.depth
                else:
                    new_node.parent = self.root
                    self.root.right = new_node
                    self.root.right.depth = 1
                    if self.root.right.depth > self.right_depth:
                        self.right_depth = self.root.right.depth
                    self.tree_size += 1

            elif new_node.val < self.root.val:
                if self.root.left:
                    self._find_home(new_node, self.root.left)
                    if new_node.depth > self.left_depth:
                        self.left_depth = new_node.depth
                else:
                    new_node.parent = self.root
                    self.root.left = new_node
                    self.root.left.depth = 1
                    if self.root.left.depth > self.left_depth:
                        self.left_depth = self.root.left.depth
                    self.tree_size += 1
        else:
            self.root = new_node
            self.tree_size += 1

    def _find_home(self, node_to_add, node_to_check):
        """.

        Check if the node_to_add belongs on the left or right
         of the node_to_check, then place it there if that spot is empty,
          otherwise recur.
        """
        if node_to_add.val > node_to_check.val:
            if node_to_check.right:
                self._find_home(node_to_add, node_to_check.right)
            else:
                node_to_add.parent = node_to_check
                node_to_check.right = node_to_add
                node_to_check.right.depth = node_to_check.depth + 1
                self.tree_size += 1

        elif node_to_add.val < node_to_check.val:
            if node_to_check.left:
                self._find_home(node_to_add, node_to_check.left)
            else:
                node_to_add.parent = node_to_check
                node_to_check.left = node_to_add
                node_to_check.left.depth = node_to_check.depth + 1
                self.tree_size += 1

    def search(self, value):
        """If a value is in the BST, return its node."""
        return self._check_for_equivalence(value, self.root)

    def contains(self, value):
        """Return whether or not a value is in the BST."""
        return bool(self.search(value))

    def _check_for_equivalence(self, value, node_to_check):
        """.

        Check if the value matches that of the node_to_check
         if it does, return the node. If it doesn't, go left or right
         as appropriate and recur. If you reach a dead end, return None.
        """
        try:
            if value == node_to_check.val:
                return node_to_check

        except AttributeError:
            return None

        if value > node_to_check.val and node_to_check.right:
            return self._check_for_equivalence(value, node_to_check.right)

        elif value < node_to_check.val and node_to_check.left:
            return self._check_for_equivalence(value, node_to_check.left)

    def depth(self):
        """Return the depth of the BST."""
        if self.left_depth > self.right_depth:
            return self.left_depth
        return self.right_depth

    def in_order(self):
        """Return a generator to perform an in-order traversal."""
        self.visited = []

        if self.root is None:
            raise IndexError("Tree is empty!")

        gen = self._in_order_gen()
        return gen

    def _in_order_gen(self):
        """Recursive helper method for in-order traversal."""
        current = self.root

        while len(self.visited) < self.tree_size:
            if current.left:
                if current.left.val not in self.visited:
                    current = current.left
                    continue

            if current.val not in self.visited:
                self.visited.append(current.val)
                yield current.val

            if current.right:
                if current.right.val not in self.visited:
                    current = current.right
                    continue

            current = current.parent

    def pre_order(self):
        """Return a generator to perform an pre-order traversal."""
        self.visited = []

        if self.root is None:
            raise IndexError("Tree is empty!")

        gen = self._pre_order_gen()
        return gen

    def _pre_order_gen(self):
        """Recursive helper method for pre-order traversal."""
        current = self.root

        while len(self.visited) < self.tree_size:
            if current.val not in self.visited:
                self.visited.append(current.val)
                yield current.val

            if current.left:
                if current.left.val not in self.visited:
                    current = current.left
                    continue

            if current.right:
                if current.right.val not in self.visited:
                    current = current.right
                    continue

            current = current.parent

    def post_order(self):
        """Return a generator to perform an post-order traversal."""
        self.visited = []

        if self.root is None:
            raise IndexError("Tree is empty!")

        gen = self._post_order_gen()
        return gen

    def _post_order_gen(self):
        """Recursive helper method for post-order traversal."""
        current = self.root

        while len(self.visited) < self.tree_size:
            if current.left:
                if current.left.val not in self.visited:
                    current = current.left
                    continue

            if current.right:
                if current.right.val not in self.visited:
                    current = current.right
                    continue

            if current.val not in self.visited:
                self.visited.append(current.val)
                yield current.val

            current = current.parent

    def breadth_first(self):
        """Return a generator to perform a breadth-first traversal."""
        self.visited = []

        if self.root is None:
            raise IndexError("Tree is empty!")

        gen = self._breadth_first_gen(self.root)
        return gen

    def _breadth_first_gen(self, root_node):
        """Helper generator for breadth-first traversal."""
        queue = [self.root]
        while queue:
            current = queue[0]
            yield current.val
            queue = queue[1:]

            if current not in self.visited:
                self.visited.append(current)

            if current.left:
                if current.left not in self.visited:
                    queue.append(current.left)

            if current.right:
                if current.right not in self.visited:
                    queue.append(current.right)

    def delete(self, val):
        """Delete the node with the given value from the tree."""
        node = self.search(val)
        if node is None:
            return

        self.tree_size -= 1
        is_root = node == self.root
        first_move_right = val > self.root.val
        last_move_right = node == node.parent.right

        if node.left is None and node.right is None:
            if is_root:
                self.root = None
                return
            if last_move_right:
                node.parent.right = None
                return
            node.parent.left = None
            return

        if node.left is None:
            if is_root:
                node.right.parent = None
                self.root = node.right
                self.root.depth = 0
                self.right_depth = self._reassess_depths(self.root.right)
                return
            if last_move_right:
                node.parent.right = node.right
                node.right.parent = node.parent

            else:
                node.parent.left = node.right
                node.right.parent = node.parent

            if first_move_right:
                self.right_depth = self._reassess_depths(node.right)
                return
            self.left_depth = self._reassess_depths(node.right)
            return

        if node.right is None:
            if is_root:
                node.left.parent = None
                self.root = node.left
                self.root.depth = 0
                self.left_depth = self._reassess_depths(self.root.left)
                return
            if last_move_right:
                node.parent.right = node.left
                node.left.parent = node.parent

            node.parent.left = node.left
            node.left.parent = node.parent
            if first_move_right:
                    self.right_depth = self._reassess_depths(node.left)
                    return
            self.left_depth = self._reassess_depths(node.left)
            return
        else:
            if is_root:
                pass

    def _reassess_depths(self, starting_node):
        """Update the depth of each node below the change and the tree."""
        self.max_depth = 0
        self._pre_order_depth_reassignment(starting_node)
        return self.max_depth

    def _pre_order_depth_reassignment(self, node):
        """Recursive helper method for pre-order depth re-assignment."""
        node.depth = node.parent.depth + 1
        if node.depth > self.max_depth:
            self.max_depth = node.depth

        if node.left:
            self._pre_order_depth_reassignment(node.left)

        if node.right:
            self._pre_order_depth_reassignment(node.right)


if __name__ == '__main__':  # pragma: no cover
    import timeit as time

    l_imba = BST([6, 5, 4, 3, 2, 1])
    r_imba = BST([1, 2, 3, 4, 5, 6])
    sample_tree = BST([20, 12, 10, 1, 11, 16, 30, 42, 28, 27])

    l_imba = time.timeit("l_imba.search(5)", setup="from __main__ import l_imba")
    r_imba = time.timeit("r_imba.search(5)", setup="from __main__ import r_imba")
    sample_tree = time.timeit("sample_tree.search(8)", setup="from __main__ import sample_tree")

    print('Left-Skewed Search Time: ', l_imba)
    print('Right-Skewed Search Time: ', r_imba)
    print('Balanced Search Time: ', sample_tree)
