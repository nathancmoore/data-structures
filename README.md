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


Binary Heap
**************************
We have implemented a Max Binary Heap. We have utilized python's list class to accomplish this. A binary heap is tree with parent and child (left and right) nodes. Left and Right child nodes are defined by the following property respectively:

2k + 1, 2k + 2

Where k is equal to list index of the parent node. We implemented the following methods as instructed. The Binary Heap is sorted according to Maximum values that satisfy the above property.

sort(): We have utilized the Bubble Sort algorithm to move nodes with highest value to the top of the heap. The use of the classic sorting algorithm drastically impacts our time complexity. Bubble Sort has a worst case of O(n^2). Any method that utilizes this method will have Big O value of O(k) + O(n^2). Any change to the heap must cause an additional sorting of the heap.

swap(): any value of greater value is assigned as the parent node. 

push(): Append value to the heap, then sort. 

pop(): Return value of lowest index, then sort, finally return the popped node.

Again, the use of Bubble Sort drastically impacts O(n) for all methods as the Binary heap must be sorted after each operation.



Priority Queue
**************************
The Priority Queue is abstract data type, meaning that we have used an existing Binary Heap to implement this
data structure. It ranks incomming values according to a priority. Our PriorityQ class is composed of our BinHeap class and makes of use of a Node Class.

It has the following methods.

Big O is largely dependent upon a Binary Heap.

sort(): As before: this is now a modification of Bubble Sort dramatically impacting all running time complexity of our priority queue. Any method that utilizes this method will have Big O value of O(k) + O(n^2). Any change to the heap must cause an additional sorting of the heap.

push(): Adds new item to the priority queue and reorders based on priority --> this uses our sort method.

pop(): Returns and removes the most important item from the queue.

peek(): Returns the most important element without removal - therefore it does not use a sort() method, so it is O(1).