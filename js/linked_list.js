"use strict"


class Node {
    constructor(val, nextNode=null) {
        this.val = val
        this.nextNode = nextNode
    }
}

class LinkedList {
    constructor(iterable=null) {
        this.root = null
        this.length = 0
        if (Array.isArray(iterable)) {
            iterable.forEach(x => this.push(x))
        }
        else if (iterable != null) {
            return 'Only arrays are valid inputs!'
        }
    }

    push(val) {
        this.root = new Node(val, this.root)
        this.length ++
    }

    pop() {
        if (!this.root) {
            return 'List is empty!'
        }
        this.length --
        let poppedValue = this.root.val
        this.root = this.root.nextNode
        return poppedValue
    }

    size() {
        return this.length
    }

    search(value) {
        let current = this.root
        while (current) {
            if (current.val == value) {
                return current
            }
            current = current.nextNode
        }
    }

    remove(node) {
        let current = this.root
        let previous = null
        while (current) {
            if (current == node) {
                this.length -= 1
                if (current == this.root) {
                    this.root = current.nextNode
                    break
                }
                previous.nextNode = current.nextNode
                break
            }
            if (current.nextNode == null) {
                return 'Given node is not in list!'
            }
            previous = current
            current = current.nextNode
        }
        return current
    }

    display() {
        let output = '('
        let current = this.root
        while (current) {
            output += current.val 
            if (current.nextNode) {
                output += ', '
            }
            current = current.nextNode
        }
        output += ')'
        return output
    }

}

module.exports = {LinkedList, Node}

// if(require.main === module){
//     var list = new LinkedList([1, 2, 3, 4])
//     console.log(list.display())
//     console.log(list.size())
//     console.log(list.remove(6))
// }