import pytest

def test_pop_empty():
    """Ensure that the pop method raises an error on an empty list."""
    from stack import Stack
    test_stack = Stack()
    with pytest.raises(IndexError):
        test_stack.pop()


def test_pop_full():
    """Ensure that pop works."""
    from stack import Stack
    test_stack = Stack()
    test_stack.push(3)
    test_stack.push(5)
    test_stack.push(7)
    assert test_stack.pop() == 7
    assert test_stack.size() == 2



def test_len():
    """Ensure that our altered len() works."""
    from stack import Stack
    test_stack = Stack()
    test_stack.push(3)
    test_stack.push(5)
    test_stack.push(7)
    assert len(test_stack) is not None
    assert len(test_stack) == 3