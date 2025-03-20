# Bit Manipulation Patterns

#### References:
- [All Types of Patterns for Bits Manipulations and How to use it](https://leetcode.com/discuss/post/3695233/all-types-of-patterns-for-bits-manipulat-qezp/)
- [Problem-list Leetcode (Bit Manipulation)](https://leetcode.com/problem-list/bit-manipulation/)

## There are 10 patterns of problems:
  ### [1] Gray code
  > [!IMPORTANT]
  > - Binary to Gray Code: XOR each bit with the previous bit:
  >   - `Gray[i]= Binary[i] ^ Binary[i−1]`
  > - Gray Code to Binary: Reverse XOR from left to right:
  >   - `Binary[i]= Gray[i] ^ Binary[i−1]`
    
```python
def binary_to_gray(n: int):       # Binary: 0000, 0001, 0010, 0011, 0100, 0101, 0110, 0111, 1000
  return n ^ (n >> 1)             # Gray:   0000, 0001, 0011, 0010, 0110, 0111, 0101, 0100, 1100

def gray_to_binary(n: int):
  result = n
  while n > 0:
    n >>= 1
    result ^= n
  return result
```

   - [x] [89. Gray Code](https://leetcode.com/problems/gray-code/description/)
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
