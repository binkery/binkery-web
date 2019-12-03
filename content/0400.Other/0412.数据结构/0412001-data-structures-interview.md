# 面试中，最重要的数据结构知识
- 面试,数据结构
- 2018.08.03

数据结构是面试中永远少不了的话题。数据结构和算法称为面试中考核一个工程师能力非常重要的标准。

数据结构是面试中永远少不了的话题。数据结构和算法称为面试中考核一个工程师能力非常重要的标准。很多公司在面试的时候非常注重数据结构和算法题，而这些题目往往是比较难的，很多人会在这方面失手。即使是多年工作经验的老手，在面试前，刷刷数据结构和算法的题目也是一种非常的需要。我们经常调侃，面试造飞机，实际拧螺丝。那能有什么办法。

1976 年，一个叫 Niklaus Wirth 计算机科学家写了一本书，Algorithms + Data Structures = Programs 。40 年过去了，这个等式还是成立的。所以在面试的时候，对数据结构和算法的考核一直是永远不变的话题。

## 什么是数据结构

a data structure is a container that stores data in a specific layout. 简单的说，数据结构就是一个容器，以一定的布局组织这些数据。这样的布局导致这些数据在某些操作中是高效的，而有些操作上低效的。我们的目标就是理解这些数据结构，在使用的时候，我们可以选出合适的一种布局。

### 为什么需要数据结构

数据结构用来以一定的组织来存储数据，而数据是计算机世界最重要的元素，所有，数据结构的重要性就不言而喻了。

不管你在解决什么问题，你总是和数据打交道，员工的薪水，股票的价格，电话本，等待。

## 常用的数据结构

 1. 数组 Arrays
 2. 栈 Stacks
 3. 队列 Queues
 4. 链表 Linked Lists
 5. 树 Trees
 6. 图 Graphs
 7. Tries
 8. 哈希表 Hash Tables

## 数组

数组是简单并且广泛使用的数据结构，栈和队列也经常是时候用数据来实现的。

数组中的每个元素都有一个表示其位置的值，称为索引 index。大部分语言中，索引是从 0 开始的。

### 数组的基本操作

数组的基本操作主要有插入、读取、删除、大小。

### 面试中常见的题目

 * 找出数组中第二小的元素
 * 找出第一个不重复的整数
 * 合并两个已经排序的数组
 * 在数组中，重新排序正值和负值

## 栈 Stacks

在很多应用中，我们都有撤销（undo）的操作。实现的思路就是类似栈的实现。

LIFO Last In First Out 是栈最显著的特征。

### 基本操作

 * Push ，插入一个元素到栈顶。
 * Pop ，从栈顶推出一个元素
 * isEmpty ， 返回栈是否是空的
 * Top ，获得栈顶的元素，但是不从栈里推出。

### 常见面试题

 * Evaluate postfix expression using a stack
 * Sort values in a stack
 * Check balanced parentheses in an expression

## 队列 Queues

队列和栈比较相似，区别是 FIFO，First In First Out，先进先出。真实生活中也是比较常见的，咱们日常排队就是这样的。

### 常见操作

 * Qnqueue() 入队
 * Dequeue() 出队
 * isEmpty() 是否为空
 * Top() 对头，有点别扭～～

### 常见面试题

 * 用队列实现一个栈 Implement stack using a queue
 * Reverse first K element of a queue
 * Generate binary numbers from 1 to n using a queue

## 链表 Linked List

链表是另外一个重要的线性的数据结构，表面上看和数组很像，但是实际上在内存上，还是有很大区别的。

链表是一个由节点组成的链，中文表达好像很别扭，英文是这样的 A linked list is like a chain of nodes 。每个节点包含数据和一个指向下一个节点的指针。链表有个头指针，指向列表的第一个元素。但这个头指针指向 null 的时候，这个列表是空的。

链表又有单向链表和双向链表。

### 基本操作

 * insert at end
 * insert at head
 * delete
 * delete at head
 * search
 * isEmpty

### 常见面试题

 * Reverse a linked list
 * Detect loop in a linked list
 * Return Nth node from the end in a linked list
 * Remove duplicates from a linked list

## 图 Graphs

图是节点的集合，这些节点以网的形式相互连接。这些节点通常被称为顶点。pair(x,y) 表示一个边，连接 x 顶点到 y 顶点。一个边包含权重或者消费的信息，显示了从 x 顶点到 y 顶点的消费。

图分为无向图和有向图，在计算机语言中，图有两种表示形式，Adjacency Matrix 相邻矩阵 和 Adjacency List 邻接表。常见的算法有广度优先算法（Breadth First Search）和深度优先算法（Depth First Search）。

### 常见的面试题
 * Implement Breadth and Depth First Search
 *　Check if a graph is a tree or not
 * Count number of edges in a graph
 * Find the shortest path between two vertices

## 树 Trees

树是由节点和连接节点的边组成的层级的数据结构。树和图有点像，关键的区别是树没有循环。树被用在人工智能和一些复杂的算法上。

树有很多种

 * N-ary Tree
 * Balanced Tree
 * Binary Tree
 * Binary Search Tree
 * AVL Tree
 * Red Black Tree
 * 2–3 Tree

### 常见的面试题

 * Find the height of a binary tree
 * Find kth maximum value in a binary search tree
 * Find nodes at “k” distance from the root
 * Find ancestors of a given node in a binary tree

## 字典树 Trie

Trie,which is also known as "Prefix Tresss"。这是一个类似于树的数据结构。经常被用来做字典单词的查找，搜索引擎的自动联想，IP 路由等。

### 常见的面试题

 * Count total number of words in Trie
 * Print all words stored in Trie
 * Sort elements of an array using Trie
 * Form words from a dictionary using Trie
 * Build a T9 dictionary

## 哈希表 Hash Table

散列算法是一种用来唯一标识对象，并且以通过键值来索引对象的方式来存储对象的一种程序。Hashing is a process used to uniquely identify objects and store each object at some pre-calculated unique index called its “key.” 所有对象被以键值对的形式存储，所以也被称为字典。每个对象都可以通过 key 被访问。

哈希表通常是通过数组来实现的。散列数据结构的性能通常以以下三个要素决定，哈希函数（Hash Function），哈希表的大小和碰撞出来方法（Collision Handling Method）。

### 常见的面试题

 * Find symmetric pairs in an array
 * Trace complete path of a journey
 * Find if an array is a subset of another array
 * Check if given arrays are disjoint

参考 ： <https://medium.freecodecamp.org/the-top-data-structures-you-should-know-for-your-next-coding-interview-36af0831f5e3>
