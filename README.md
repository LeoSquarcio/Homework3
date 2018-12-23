# Homework3

This project has the purpose to analyze which algorithm between: QuickSort, BubbleSort,the node based Binary-Search Tree and HeapSort is the fastest in sorting a random integer n  (0 < n < 1000).
the code will return the maximum and the minimum integer in the list.

The QuickSort algorithm first selects a value, which is called the pivot value, and it's selected around the middle of the list. This pivot will assist the splitting of a list of length n, producing a number of divisions = log(n).  
In order to find the split point, each of the n items needs to be compared to the pivot value.
To return the minimum and the maximum value we returned the element of index[0] and the element of index[-1] of the sorted list.
In terms of Execution time of the Code, the return of the minimum and maximum value has an execution time very close to zero, while the only part of the code that needs time to run was the element sorting, which increases with the amount of elements in the List.



The BubbleSort algorithm compares all the element in a list of lenght n, one by one like if they were closed in a "Bubble". Then, it sorts them based on their values: for example, if the first element is greater than the second element, it will swap both the elements moving on to compare the other. 
This process have to be repeated n-1 times, regardless of the original arrangement of the list.

To obtain the MIN and the MAX values, it's enough to return respectively the elements of index[0] and index[-1] 
Just like in the QuickSort, method, the time needed to retrieve the MIN and the MAX value was almost zero, but at the same time the BubbleSort method is a lot faster in the adding process.



An Heap is a special tree structure in which each node less than or equal to its "child" node is called a Min Heap.Otherwise, if each parent node is greater than or equal to its child node then it is called a max heap. It is very useful is implementing priority queues where the queue item with higher weightage is given more priority in processing.
A heap is created by using python’s inbuilt library named "heapq". This library has the relevant functions to carry out various operations on heap data structure.
The Add operation of the Heapis slightly faster compared to QuickSort and BubbleSort, and the Heap has a constant speed in finding the Maximum value, but it's also the slowest to find the Minimum value.


Binary Search Tree is a node-based binary data structure which looks very similar to a "family Tree", with some specific properties: every left "subtree" of a node contains only nodes with smaller keys than the previous node. Every right subtree, on the other hand, contains only nodes with biggers keys than the previous node.
The left and right subtree each must also be a binary search tree, so those properties remain contant for "parents" and "childs". 

On average a Binary Search tree with n node have O(log(n)) height and searching requires time proportional to the height of the tree, which is O(log(n))
Both the add operation and the return of the MIN and the MAX value are faster than the ones of QuickSort and BubbleSort, but slower than the HeapSort ones.
 
 
 

In order to measure the time of execution, we have to import other inbuilt Python libraries, the random library and the time library.
Timeit works by running the setup code once and then make repeated calls to a series of statements.
The execution time is measured in milliseconds ("msec").
