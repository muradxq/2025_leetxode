# Bit Manipulation Patterns

#### References:
- [All Types of Patterns for Bits Manipulations and How to use it](https://leetcode.com/discuss/post/3695233/all-types-of-patterns-for-bits-manipulat-qezp/)
- [Problem-list Leetcode (Bit Manipulation)](https://leetcode.com/problem-list/bit-manipulation/)

## There are 10 patterns of problems:
  ### [1] Gray code
  > [!IMPORTANT]
  > - The formula to convert a binary number to Gray code:
  >   - Gray[i]= Binary[i] ^ Binary[i−1]
  > - The formula to convert gray code to binary number :
  >   - Binary[i]= Gray[i] ^ Binary[i−1]
    
    ```python
      def binary_search(array):
        def condition(value):
            pass
    
        left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left
      ```

   - [ ] [89. Gray Code](https://leetcode.com/problems/gray-code/description/)
   - [ ] [1238. Circular Permutation in Binary Representation](https://leetcode.com/problems/circular-permutation-in-binary-representation/description/)
  ### 2. N is power of p
   > [!IMPORTANT]
   > num is power of p
   - [ ] [231. Power of Two](https://leetcode.com/problems/power-of-two/description/)
   - [ ] [326. Power of Three](https://leetcode.com/problems/power-of-three/description/)
   - [ ] [342. Power of Four](https://leetcode.com/problems/power-of-four/description/)
  ### 3. Question on the Basic properties of XOR
   > [!IMPORTANT]
   > - xor of a same number with itself is zero, i.e A ^ A = 0
   > - xor is commutative that means a ^ b = b ^ a.
   > - xor of any number with zero is the number itself i.e A ^ 0 = A.
   - [ ] [136. Single Number](https://leetcode.com/problems/single-number/description/)
   - [ ] [137. Single Number II](https://leetcode.com/problems/single-number-ii/description/)
   - [ ] [260. Single Number III](https://leetcode.com/problems/single-number-iii/description/)
   - [ ] [2433. Find The Original Array of Prefix Xor](https://leetcode.com/problems/find-the-original-array-of-prefix-xor/description/)
   - [ ] [1442. Count Triplets That Can Form Two Arrays of Equal XOR](https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/description/)
   - [ ] [1310. XOR Queries of a Subarray](https://leetcode.com/problems/xor-queries-of-a-subarray/description/)
          
  ### 4. Based On fact Seting Left most bit give You Large Number
  ### 5. DP + Bitmasks
  ### 6. Restricting Over some Operation e.g. -> + and - and / etc
  ### 7. We can Hash any string to bit mask
  ### 8. Decode XORed Array.
  ### 9. Generating submasks of a bitmask
  ### 10. Kth bits questions
