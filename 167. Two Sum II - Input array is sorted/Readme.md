题目
====
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

思路
====
这道题是可以用两层循环蛮力解决的，但是效率太低了。我们如何能得到一个复杂度为n的解法呢？
我们可以声明两个指针left，right分别指向数组中最小的元素、最大的元素。
如果这两个元素和大于目标数组，right指针左移；如果小于，left指针右移。如果等于，则返回这两个元素的位置（记得用数组的index数值加一）
