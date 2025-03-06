# Heap (Priority Queue) Patterns

#### References:
- [Master HEAP: Understanding 4 patterns where HEAP data structure is used](https://leetcode.com/discuss/general-discussion/1127238/master-heap-by-solving-23-questions-in-4-patterns-category)


## Introduction
The objective of this tutorial is to understand the basics of Heap, time complexities, and identify patterns when to use Heap as a data structure.

### What is Heap?
- It is mainly used to represent a **priority queue**.
- It is represented as a complete binary trees.
- A simple array can be used to represent a Heap where array indices refer to the node position in the tree.
- Parent and child nodes can be accessed with indices:
  - A root node｜i = 0, the first item of the array
  - A parent node｜`parent(i) = i / 2`
  - A left child node｜`left(i) = 2i`
  - A right child node｜`right(i)=2i+1`
- Two type of Heaps — Min Heap, Max Heap
  - `Min Heap` — the parent node always has a smaller value than the child nodes.
  - `Max Heap` — the parent node is always larger than the child node value.
- Usually, when a type is not mentioned, it refers to the MinHeap. Python Heap has minHeap as default.
- In python, the heapq module provides the basic features for Heap data structure.
- minHeap are used in tasks related to scheduling or assignment. A more detailed explanation is under the Patterns section below.


### Heap in Python
 The basic operations in Python heapq are:
 #### 1- heapify
 The heapify operation converts the iterable array heap into a tree structure w.r.t heap order.
 #### 2- heappush
 It inserts an element into the heap. Post insertion the heap order is adjusted to maintain the heap properties.

  ```python
  import heapq as hq
  # Simple array is heap
  minHeap = []
  # Adding an element to the heap
  hq.heappush(minHeap, 5)
  ```

 #### 3- heappop
  This operation is to remove the element from the heap. By default it is minHeap, so this operation removes the min element from the minHeap. And for maxHeap, it is the maximum element. Post removal, heapify is called internally to maintain the heap order.

  ```python
  import heapq as hq
  minHeap = [5, 6, 2]
  # this is done to convert iterable into a heap tree
  hq.heapify(minHeap) 
  # Getting top element from the heap
  value = hq.heappop(minHeap) # the value here is 2 as 2 is the minimum value. 
  ```
Other operations in heapq python module includes heappushpop ,heapreplace , nlargest , nsmallest.



