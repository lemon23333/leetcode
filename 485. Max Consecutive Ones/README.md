题目
===
找出1的最大连续数
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

思路
===
遇到1时，计数+1，遇到0时，计数若大于当前最大计数，则更新，随后=0

code1：比较是自己写的方法，代码量大，但运行时间短
---
code2：比较时用的max（）方法，代码简洁，但运行时间稍长
---
