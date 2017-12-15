'use strict';

let linkedList = require('../linked_list');
let chai = require('chai');
let expect = chai.expect;

describe('linked_list.js tests', () => {
    it('can you pass in an iterable to a new list?', () => {
        let testList = new linkedList.LinkedList([1, 2, 3]);
        expect(testList.size()).to.equal(3);
        expect(testList.root.val).to.equal(3);
    });

    it('does push add a new value?', () => {
        let testList = new linkedList.LinkedList();
        testList.push(60);
        expect(testList.root.val).to.equal(60);
    });

    it("does push reassign the root?", () => {
        let testList = new linkedList.LinkedList();
        testList.push(5);
        testList.push(10);
        expect(testList.root.val).to.equal(10);
    });

    it("does pop return the value of the root?", () => {
       let testList = new linkedList.LinkedList();
       testList.push(320);
       testList.push(420);
       expect(testList.root.val).to.equal(420);
       expect(testList.pop()).to.equal(420);
    });

    it("does pop reassign the root?", () => {
        let testList = new linkedList.LinkedList();
        testList.push(1);
        testList.pop();
        expect(testList.pop()).to.equal('List is empty!');
        testList.push(1);
        testList.push(2);
        testList.pop();
        expect(testList.root.val).to.equal(1);
    });

    it("does size return the proper value?", () => {
        let testList = new linkedList.LinkedList();
        expect(testList.size()).to.equal(0);
        testList.push(1);
        expect(testList.size()).to.equal(1);
        testList.push(2);
        expect(testList.size()).to.equal(2);
        testList.pop();
        expect(testList.size()).to.equal(1);

    });

    it("does a bad search return null?", () => {
       let testList = new linkedList.LinkedList();
       testList.push(1);
       expect(testList.search(2)).to.be.undefined;
    });

    it("does search returns a Node object?", () => {
        let testList = new linkedList.LinkedList();
        testList.push(10);
        testList.push(20);
        expect(testList.search(10)).to.be.an.instanceof(linkedList.Node);
        expect(testList.search(10).val).to.be.equal(10);
    });

    it("does remove work?", () => {
        let testList = new linkedList.LinkedList();
        testList.push(1);
        testList.remove(testList.search(1));
        expect(testList.size()).to.equal(0);
        expect(testList.root).to.be.null;
        testList.push(2);
        testList.push(3);
        testList.push(4);
        testList.remove(testList.search(3));
        expect(testList.root.val).to.equal(4);
        expect(testList.size()).to.equal(2);
    });

    it("does display work?", () => {
        let testList = new linkedList.LinkedList();
        testList.push(1);
        testList.push(2);
        testList.push(3);
        testList.push(4);
        expect(testList.display()).to.be.string('4, 3, 2, 1');
    });
});