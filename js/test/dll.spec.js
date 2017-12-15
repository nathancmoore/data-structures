'use strict';

let dll = require('../dll');
let chai = require('chai');
let expect = chai.expect;

describe('dll.js tests', () => {
    it('can you pass in an iterable to a new list?', () => {
        let testList = new dll.DLL([1, 2, 3]);
        expect(testList.size()).to.equal(3);
        expect(testList.head.val).to.equal(1);
        expect(testList.tail.val).to.equal(3);
    });

    it('does push add a new value?', () => {
        let testList = new dll.DLL();
        testList.push(60);
        expect(testList.head.val).to.equal(60);
        expect(testList.tail.val).to.equal(60);
    });

    it("does push reassign the head and tail?", () => {
        let testList = new dll.DLL();
        testList.push(5);
        testList.push(10);
        expect(testList.head.val).to.equal(10);
        expect(testList.tail.val).to.equal(5);
    });

    it('does append add a new value?', () => {
        let testList = new dll.DLL();
        testList.append(60);
        expect(testList.head.val).to.equal(60);
        expect(testList.tail.val).to.equal(60);
    });

    it("does append reassign the head and tail?", () => {
        let testList = new dll.DLL();
        testList.append(5);
        testList.append(10);
        expect(testList.head.val).to.equal(5);
        expect(testList.tail.val).to.equal(10);
    });

    it("does pop return the value of the head?", () => {
       let testList = new dll.DLL();
       testList.push(320);
       testList.push(420);
       expect(testList.head.val).to.equal(420);
       expect(testList.pop()).to.equal(420);
    });

    it("does pop reassign the head?", () => {
        let testList = new dll.DLL();
        testList.push(1);
        testList.pop();
        expect(testList.pop()).to.equal('List is empty!');
        testList.push(1);
        testList.push(2);
        testList.pop();
        expect(testList.head.val).to.equal(1);
    });

    it("does shift return the value of the tail?", () => {
       let testList = new dll.DLL();
       testList.push(320);
       testList.push(420);
       expect(testList.tail.val).to.equal(320);
       expect(testList.shift()).to.equal(320);
    });

    it("does shift reassign the head?", () => {
        let testList = new dll.DLL();
        testList.push(1);
        testList.shift();
        expect(testList.shift()).to.equal('List is empty!');
        testList.push(1);
        testList.push(2);
        testList.shift();
        expect(testList.head.val).to.equal(2);
    });

    it("does size return the proper value?", () => {
        let testList = new dll.DLL();
        expect(testList.size()).to.equal(0);
        testList.push(1);
        expect(testList.size()).to.equal(1);
        testList.append(2);
        expect(testList.size()).to.equal(2);
        testList.pop();
        expect(testList.size()).to.equal(1);

    });

    it("does remove work?", () => {
        let testList = new dll.DLL();
        testList.push(1);
        testList.remove(1);
        expect(testList.size()).to.equal(0);
        expect(testList.head).to.be.null;
        expect(testList.tail).to.be.null;
        testList.push(2);
        testList.push(3);
        testList.push(4);
        testList.remove(3);
        expect(testList.head.val).to.equal(4);
        expect(testList.tail.val).to.equal(2);
        expect(testList.size()).to.equal(2);
    });
});