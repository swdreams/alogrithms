#Find the minimum number of moves to reach end of the array

Given an array arr[] of size N where every element is from the range [0, 9]. The task is to reach the last index of the array starting from the first index. From ith index we can move to (i – 1)th, (i + 1)th or to any jth index where j ≠ i and arr[j] = arr[i].

Examples:
```
Input: arr[] = {1, 2, 3, 4, 1, 5}
Output: 2
First move from the 0th index to the 4th index
and then from the 4th index to the 5th.
```

```
Input: arr[] = {1, 2, 3, 4, 5, 1}
Output: 1
```

Approach: Construct the graph from the given array where the number of nodes in the graph will be equal to the size of the array. Every node of the graph i will be connected to the (i 1)th node, (i + 1)th node and a node j such that i ≠ j and arr[i] = arr[j]. Now, the answer will be the minimum edges in the path from index 0 to index N – 1 in the constructed graph.
The graph for the array arr[] = {1, 2, 3, 4, 1, 5} is shown in the image below:

![1 copy 2x](https://media.geeksforgeeks.org/wp-content/uploads/20190922014120/g132-300x297.png)
