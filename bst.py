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

    def balance(self, starting_node=None):
        """Return the current balance of a tree or subtree."""
        if not starting_node:
            return self.right_depth - self.left_depth

        r_depth = 0
        l_depth = 0

        if starting_node.right:
            r_depth += self._reassess_depths(starting_node.right)

        if starting_node.left:
            l_depth += self._reassess_depths(starting_node.left)

        return r_depth - l_depth

    def size(self):
        """Return the current size of the BST."""
        return self.tree_size

    def insert(self, value):
        """Insert a new node into the BST, and adjust the balance."""
        new_node = Node(value)
        self.tree_size += 1

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

        else:
            self.root = new_node

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
                # self._rebalance(node_to_add.parent)

        elif node_to_add.val < node_to_check.val:
            if node_to_check.left:
                self._find_home(node_to_add, node_to_check.left)
            else:
                node_to_add.parent = node_to_check
                node_to_check.left = node_to_add
                node_to_check.left.depth = node_to_check.depth + 1
                # self._rebalance(node_to_add.parent)

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

    def depth(self, starting_node=None):
        """Return the depth of the tree or subtree."""
        if not starting_node:
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
        if node.parent:
            last_move_right = node == node.parent.right
        else:
            last_move_right = False

        if node.left is None and node.right is None:
            if is_root:
                self.root = None
                return
            if last_move_right:
                node.parent.right = None
                # self._rebalance(node.parent)
                return
            node.parent.left = None
            # self._rebalance(node.parent)
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
                # self._rebalance(node.parent)
                return
            self.left_depth = self._reassess_depths(node.right)
            # self._rebalance(node.parent)
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
                    # self._rebalance(node.parent)
                    return
            self.left_depth = self._reassess_depths(node.left)
            # self._rebalance(node.parent)
            return
        else:
            replacement_node = self._locate_replacement_node(node)
            self.delete(replacement_node.val)

            if is_root:
                self.root = replacement_node
                replacement_node.parent = None
                replacement_node.depth = 0

            else:
                replacement_node.parent = node.parent
                replacement_node.depth = node.depth

            replacement_node.left = node.left
            replacement_node.right = node.right
            node.left.parent = replacement_node
            node.right.parent = replacement_node
            if first_move_right or is_root:
                self.right_depth = self._reassess_depths(self.root.right)

            else:
                self.left_depth = self._reassess_depths(self.root.left)

            # if node.parent:
                # self._rebalance(node.parent)
            return

    def _reassess_depths(self, starting_node):
        """Fix the depth of nodes below the starting_node an return the max_depth."""
        self.max_depth = 0

        if starting_node:
            self.visited = []
            queue = [starting_node]
            while queue:
                current = queue[0]
                current.depth = current.parent.depth + 1
                if current.depth > self.max_depth:
                    self.max_depth = current.depth
                queue = queue[1:]

                if current not in self.visited:
                    self.visited.append(current)

                if current.left:
                    if current.left not in self.visited:
                        queue.append(current.left)

                if current.right:
                    if current.right not in self.visited:
                        queue.append(current.right)

        return self.max_depth - starting_node.parent.depth

    def _locate_replacement_node(self, starting_node):
        """Return the lowest-valued node on the right side of the sub-tree."""
        current = starting_node.right
        while current.left:
            current = current.left
        return current

    def _rebalance(self, node):
        """Rebalance a subtree, and if its root has a parent, recur on it."""
        node_balance = self.balance(node)

        if node_balance == 2:
            child_balance = self.balance(node.right)

            if child_balance == 1:
                self._rotate_left(node)

            if child_balance == -1:
                self._rotate_right(node.right)
                self._rotate_left(node)

        if node_balance == -2:
            child_balance = self.balance(node.left)

            if child_balance == 1:
                self._rotate_left(node.left)
                self._rotate_right(node)

            if child_balance == -1:
                self._rotate_right(node)

        # if node.parent:
            # self._rebalance(node.parent)

    def _rotate_left(self, node):
        """Rotate a node leftwards around its right child."""
        pivot_node = node.right

        if node.parent:
            node.parent.left = pivot_node

        else:
            self.root = pivot_node

        pivot_node.parent = node.parent
        node.parent = pivot_node

        if pivot_node.left:
            pivot_node.left.parent = node

        node.right = pivot_node.left
        pivot_node.left = node

    def _rotate_right(self, node):
        """Rotate a node rightwards around its left child."""
        pivot_node = node.left

        if node.parent:
            node.parent.right = pivot_node

        else:
            self.root = pivot_node

        pivot_node.parent = node.parent
        node.parent = pivot_node

        if pivot_node.right:
            pivot_node.right.parent = node

        node.left = pivot_node.right
        pivot_node.right = node


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
