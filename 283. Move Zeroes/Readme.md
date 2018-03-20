
题目
========
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

思路
======
code1：排序
遍历list，零值与后一个非零值交换
code2：直接找非零值
遍历list，非零值依次往前放，后面用零补齐

比较
======
code2方法比较直接，运行时间较快50+ms，code1 1000+ms
