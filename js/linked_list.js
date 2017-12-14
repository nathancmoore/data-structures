
"use strict";


class Node {
    constructor(val, nextNode=null) {
        this.val = val;
        this.nextNode = nextNode;
    }
}

class LinkedList {
    constructor(iterable=null) {
        this.root = null;
        this.size = 0;
        if (Array.isArray(iterable)) {
            iterable.forEach(x => this.push(x));
        }
        else {
            throw 'Only arrays are valid inputs!';
        }
    }

    push(val) {
        this.root = new Node(val, this.root);
        this.size ++;
    }

    pop() {
        if (!this.root) {
            throw 'List is empty!';
        }
        poppedValue = this.root.val;
        this.root = this.root.nextNode;
        return poppedValue;
    }