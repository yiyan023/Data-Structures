# Data Structures and Algorithms 👩‍💻
Hey there 👋! This repository is dedicated for building my knowledge of data structures and algorithms, where it includes most of the Leetcode solutions I have written for various problems. Here are some of the things I have learned:

## Algorithms: 

### Sliding Window 🪟:
- Used to perform a required operation on a specific window size
- Useful for linked list & arrays

### Two Pointer ✌️: 
- two pointers iterate through the data structure until at least one pointer hits a certain condition
- useful for earching pairs in a sorted array or linked list

### Fast & Slow Pointers 🐢:
- pointer algorithm that uses two pointers which move through the array at different speeds
- used for dealing with cyclic linked lists / arrays
- also known as Floyd’s Algorithm

### Breadth First Search (BFS) 🌴:
- traverses a tree / graph and uses a queue to keep track of all the nodes on a level before jumping onto the next level
- for a tree, this would be all the node at the same height
- for a graph, this would be all the neighbours of the current cell

### Depth First Search (DFS) 🌊:
- uses recursion or iteration with a stack to to keep track of all the previous (parent) nodes while traversing a tree
- the process of going as “deep” as possible
- used for trees and graphs
- for a tree, you traverse its children nodes & continue traversing until you reach the leaf node
- for a graph, you traverse along one path until you reach a certain condition or cannot go in this path anymore

### Binary Search 👀:
- used to find a certain element in a sorted array, linked list, matrix, or numbers 1-n by comparing the median / middle value to the desired value
- The array size is split into half each time depending on whether the current median is greater / less than / equal to the desired value
- O(log n) time complexity

### Greedy 🤢:
- makes locally optimal choices at each step
- similar to dynamic programming but is often used for true / false problems that do not require a numeric answer

### Backtracking 🔙:
- recursive algorithm used for finding total possibilities that fit under a specific condition

### Dynamic Programming 📩:
- to optimize recursive problems, which are dependent on previous values / smaller instances of the same problem
- process of continually updating stored values

## Data Structures: 
- **Hash map:** stores data in key-value pairs
- **Stack:** stores data with first in, last out order
- **Queue:** stores data with first in, first out order
- **Heap:** BST that satisfies the heap property — the children of a tree is always less than / greater than the node (root is either greatest or smallest in a tree)
- **Graph:** abstract data type that can be used to represent complex, non-linear relationships between objects
- **Trees:** sorted tree where left children are always less than the root and the right children are always greater than the root, primarily deal with Binary Search Trees (BSTs)
- **Tries:** a trie is a tree data structure used to store strings over the alphabet
- **Linked Lists:** a sequence of nodes, which contains a data value & a link or pointer to the next node
- **Set:** unordered list with unique elements
