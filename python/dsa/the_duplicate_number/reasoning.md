If using extra space is allowed, just use a `set` to track seen elements. But the desired space complexity is $O(1)$. 

So, let us start from the beginning.

Given $(n + 1)$ integers such that every value is within the interval $[1, n]$. Only one of the numbers is repeated two or more times. That implies:

* All the elements are greater than 0.
* Every value can be used as an _index_ to access another value.

So, traverse the array. In every iteration, negate the value at the index represented by the current number. The idea is that when an index repeats, its corresponding value would already be _negative_, indicating that the current number is the required duplicate.

Unfortunately, we are not allowed to mutate the given array. To respect the constraints, pose the algorithm as creating a linked list, where every value represents the pointer to the next node. 

* Such a list will always have a cycle.
* No. of incoming links is equal to the no. of times the node index appears in the array, which implies the node with the repeated index has more than one incoming links. Hence, the duplicate number is the entry point to the cycle.