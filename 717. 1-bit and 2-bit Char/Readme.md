题目
===
We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:
Input: 
bits = [1, 0, 0]
Output: True
Explanation: 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
Example 2:
Input: 
bits = [1, 1, 1, 0]
Output: False
Explanation: 
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
Note:

1 <= len(bits) <= 1000.
bits[i] is always 0 or 1.

思路
=====
code1：56ms，倒数第二个数如果是1，往前数连续的1的个数，个数为奇数时False，其他情况为偶数，注意区分列表数量为1时。
code2：48ms，从前往后数，遇到1，跳数，遇到0，顺序访问，比较最后一个数访问位置
code3：44ms，与code1有相似，使用堆栈和亦或方法，代码更简洁
