# data-structures



Singly Linked List
******************
We have implemented a singly linked list using a Node and Linked List Class.

We have the following methods. Additionally, we have overwritten the existing methods for len()
and str() to reflect the size and contents of the list.

Push
Insert new Node to the front of the list.

Search
Return a node if it is contained in the list.

Remove
Delete a node from the list.

Pop
Return the head of a list and then delete it.

Display
Print the contents of the List.


Time Complexity
*************

Push,Pop, and Remove are constant time, O(1), because elements are inserted/removed from a known index.
Search and Display are O(n) because all contained elements must be accessed.





Stack Data Structure
*******************

We have implemented a stack data structure using a linked list. We use composition to utilize the existing
methods of the our previous Linked List Class.

Methods:

Push
The Push method inserts a new node adjusts the pointers such that the new node becomes the head of a list.

Pop
The Pop method returns the first node in a list, then removes it from the list.

Time Complexity.
Neither of these methods requires iteration through a list of elements. An element is merely selected and returned.
This is Constant Time or O(1).

Doubly-Linked List
******************
We have implemented a doubly linked list. We now have to take into account the previous node during all operations.
Nodes point in both directions now. For example, if a node of a middle value is removed --> the previous node
must point to the node ahead of the current.

Push
Insert new Node to the front of the list.

Search
Return a node if it is contained in the list.

Remove
Delete a node from the list.

Pop
Return the head of a list and then delete it.

Display
Print the contents of the List.

Shift 
Return and remove tail node from list.

Append
Add new tail to the end of the list.

Time Complexity.
Shift and Append are of constant time, O(1) whereas any method which utilizes iteration throughout list is 
O(n) --> example search, display.

Queue
*********************
We have implemented a Queue class utilizing a doubly linked list. 

Enqueue
Adds a new element to the end of a list. The new item becomes the tail, the current tail becomes the next element.

Dequeue
Returns and removes the head of the list. The previous node now becomes the new head.

Size
Returns the size of the queue --> The starts from the first element in the queue and works its way backward.

Peak
Returns without removal the first element in the queue.

Time Complexity.
As before any insertion or deletion is O(1). Attempts to access the Queue are O(n).


Deque
*********************
We have created a Deque class, which is a doubly-linked list which can be appended to or popped from either the right or left of the list.

It has the following methods:

size(): Measures the number of nodes in the deque, with a time complexity of O(n)

pop(): removes and returns the tail node, with a time complexity of O(1)

popleft(): removes and returns the head node, with a time complexity of O(1)

append(): adds a new node to the tail of the list, with a time complexity of O(1)

appendleft(): adds a new node to the head of the list, with a time complexity of O(1)

peek(): returns the value of the tail of the list, with a time complexity of O(1)

peekleft(): returns the value of the head of the the list, with a time complexity of O(1)