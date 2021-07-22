### 描述
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
示例1
输入：
[1,2,3,4,5],[4,3,5,1,2]
复制
返回值：
false

Given two sequences `pushed` and `popped` **with distinct values**, return `true` if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.

  

**Example 1:**

```
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
```

**Example 2:**

```
Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
```

 

**Constraints:**

- `0 <= pushed.length == popped.length <= 1000`
- `0 <= pushed[i], popped[i] < 1000`
- `pushed` is a permutation of `popped`.
- `pushed` and `popped` have distinct values.
### 分析
1. 定义两个指针分别指向pushedV和popedV，并且定义一个辅助栈S
2. 如果S栈顶元素不等于popedV[j], 推入pushedV[i] i++
3. 如果S栈顶元素等于popedV[j]，弹出栈顶元素，j++
4. 判断步骤3，如果满足继续弹出，如果不满足走步骤2
5. return is S.isEmpty()