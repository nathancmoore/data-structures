"use strict"


class Node {
    constructor(val, nextNode=null, prevNode=null) {
        this.val = val
        this.nextNode = nextNode
        this.prevNode = prevNode
    }
}

class DLL {
    constructor(iterable=null) {
        this.head = null
        this.tail = null
        this.length = 0
        if (Array.isArray(iterable)) {
            iterable.forEach(x => this.append(x))
        }
        else if (iterable != null) {
            return 'Only arrays are valid inputs!'
        }
    }

    push(val) {
        this.length ++
        var newNode = new Node(val, this.head)
        if (this.length == 1) {
            this.tail = newNode
        }
        else if (this.length == 2) {
            this.tail = this.head
            this.tail.prevNode = newNode
        }
        else {
            this.head.prevNode = newNode
        }
        this.head = newNode
    }

    append(val) {
        this.length ++
        var newNode = new Node(val, null, this.tail)
        if (this.length == 1) {
            this.head = newNode
        }
        else if (this.length == 2) {
            this.head = this.tail
            this.head.nextNode = newNode
        }
        else {
            this.tail.nextNode = newNode
        }
        this.tail = newNode
    }

    pop() {
        if (!this.head) {
            return 'List is empty!'
        }
        this.length --
        let poppedValue = this.head.val
        this.head = this.head.nextNode
        if (this.length > 0) {
            this.head.prevNode = null
        }
        else {
            this.tail = null
        }
        return poppedValue
    }

    shift() {
        if (!this.tail) {
            return 'List is empty!'
        }
        this.length --
        let poppedValue = this.tail.val
        this.tail = this.tail.prevNode
        if (this.length > 0) {
            this.tail.nextNode = null
        }
        else {
            this.head = null
        }
        return poppedValue
    }

    size() {
        return this.length
    }

    remove(value) {
        let current = this.head
        let previous = null
        while (current) {
            if (current.val == value) {
                this.length --
                if (this.length == 0) {
                    this.head = null
                    this.tail = null
                    break
                }
                else if (this.length == 1) {
                    if (current == this.head) {
                        this.head = this.tail
                        this.tail.prevNode = null
                    }
                    else {
                        this.tail = this.head
                        this.head.nextNode = null
                    }
                    break
                }
                else {
                    if (current == this.head) {
                        this.head = this.head.nextNode
                        this.head.prevNode = null
                    }
                    else if (current == this.tail) {
                        this.tail = this.tail.prevNode
                        this.tail.nextNode = null
                    }
                    else {
                        current.nextNode.prevNode = current.prevNode
                        current.prevNode.nextNode = current.nextNode
                    }
                    break
                }
            }
            if (current.nextNode == null) {
                return 'Given node is not in list!'
            }
            previous = current
            current = current.nextNode
        }
        return current.val + ' has been removed.'
    }
}

module.exports = {DLL, Node}