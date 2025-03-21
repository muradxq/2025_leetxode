# Monotonic Stack

#### References:
- [A comprehensive guide and template for monotonic stack based problems](https://leetcode.com/discuss/study-guide/2347639/A-comprehensive-guide-and-template-for-monotonic-stack-based-problems)

### Introduction
There are four types of monotonic stacks:
| Type  | Description |  Example |
|:----------|:----------|:----------|
| **Strictly Increasing**  | Every element of the stack is strictly greater than the previous element.     | `[1, 4, 5, 8, 9, 10]`    |
| **Non-Decreasing**       | Every element of the stack is greater than or equal to the previous element.  | `[1, 4, 5, 5, 8, 9, 9]`  |
| **Strictly Decreasing**  | Every element of the stack is strictly smaller than the previous element.     | `[9, 8, 5, 4, 2, 1, 0]`  |
| **Non-Increasing**       | Every element of the stack is smaller than or equal to the previous element.  | `[9, 9, 8, 5, 5, 4, 1]`  |

 #### Template:
 ```python
 # At all points in time, the stack maintains its monotonic property
 def buildMonoStack(nums):
   # Initialize an empty stack
   stack = []
   # Iterate through all the elements in the array
   for i in range(len(nums)):
     while ((len(stack) != 0) and stack top `OPERATOR` nums[i]):
        # If the previous condition is satisfied, we pop the top element
        stackTop = stack.pop()
        # Do something with stackTop here (nextGreater[stackTop] = i)
     if (len(stack) !=0):
        # If stack has some elements left
        # Do something with stack top here (previousGreater[i] = stack[-1])

     # At the end, we push the current index into the stack
     stack.push(i)    
 ```
 #### Notes about the template above
 > [!IMPORTANT]
 > - We initialize an empty stack at the beginning.
 > - The stack contains the index of items in the array, not the items themselves
 > - There is an outer for loop and inner while loop.
 > - At the beginning of the program, the stack is empty, so we don't enter the while loop at first. 
 > - At the end of the while loop, the index of the current element is pushed into the stack
 > - The `OPERATOR` inside the while loop condition decides what type of monotonic stack are we creating.
 > - The `OPERATOR` could be any of the four `>, >=, <, <=`
 
 > [!IMPORTANT]
 > - **Time complexity**:  `O(n)` Because no element is accessed more than four times (constant). 
 > - **Space complexity**: `O(n)` Because we are using an external data structure (stack).
 
 > [!IMPORTANT]
 > - In our implementation:
 >  -  Finding `next greater` and `previous greater` elements require building a monotone `decreasing` stack.
 >  -  Finding `next smaller` and `previous smaller` requires building a monotone `increasing` stack.
 
 ## There are Four Patterns:
  ### [1] Next Greater
  > [!IMPORTANT]
  > Given the following array, Find the next greater element for each item.
  > - `nums  = [13, 8, 1, 5, 2, 5, 9, 7, 6, 12]`
  > - `NextG = [null, 9, 5, 9, 5, 9, 12, 12, 12, null]`
  > - For finding next greater elements (not equal) we use a monotonic non increasing stack (type 4)
  > - If the question was to find next greater or equal elements, then we would have used a monotonic strictly decreasing stack (type 3)
  > - We use the operator < in while loop condition above - this results in a monotonic non increasing stack (type 4).
  > - If we use <= operator, then this becomes a monotonic strictly decreasing stack (type 3)
  > - Time and space complexity - `O(n)`.
   
 ```python
 def findNextGreaterIndex(nums):
   # Initialize an empty stack
   stack = []
   # Initialize nextGreater array with -1, this array hold the output
   nextGreater =[-1]*len(nums)
   # Iterate through all the elements of the array
   for i in range(len(nums)):
      # while loop runs until the stack is not empty AND
      # the element represented by stack top is STRICTLY SMALLER than the current element
      # This means, the stack will always be *monotonic non increasing (type 4)*
      while ((len(stack) != 0) and nums[stack[-1]] < nums[i]):
         # Pop out the top of the stack, it represents the index of the item
         stackTop = stack.pop()
         # As given in the condition of the while loop above, nextGreater element of stackTop is the element at index i
         nextGreater[stackTop] = i
 
      # Push the current element
      stack.push(i)
    return nextGreater
 ```



  ### [2] Previous Greater	
  > [!IMPORTANT]
  >  decreasing (equal allowed)	
    
 ```python
 def binary_to_gray(n: int):      
  
 ```

  ### [3] Next Smaller	
  > [!IMPORTANT]
  >  decreasing (equal allowed)	
    
 ```python
 def binary_to_gray(n: int):      
  
 ```

  ### [4] Previous Smaller	
  > [!IMPORTANT]
  >  decreasing (equal allowed)	
    
 ```python
 def binary_to_gray(n: int):      
  
 ```

### Problems: 
- [x] [278. First Bad Version](https://leetcode.com/problems/first-bad-version/description/) 
