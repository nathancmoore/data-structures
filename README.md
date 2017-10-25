# data-structures



Singly Linked List
******************
We have implemented a singly linked list using a Node and Linked List Class.

We have the following methods

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