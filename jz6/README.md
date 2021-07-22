### 题目
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

输入：[3,4,5,1,2] 返回：1


### 分析
***二分法***

注意原始数组为一个非递减数组，所以翻转后的数组可以分为前后两个区间，且两个区间分别为连个非递减子数组，其中前面区间的最小值也比后面区间的最大值要大（因为原本就是一个非递减数组），
利用这个特性可以使用二分法解决。
```python
# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        # write code here
        low = 0
        high = len(rotateArray) - 1
        mid = int(len(rotateArray) / 2)

        while low < high:
            if rotateArray[low] < rotateArray[high]:
                # 如果已经在一个递增区间了，那就可以直接返回了
                return rotateArray[low]
            if rotateArray[low] < rotateArray[mid]:
                # mid处在前区间，low上移
                low = mid + 1
            elif rotateArray[mid] < rotateArray[high]:
                # mid在后区间，high下移
                high = mid
            else:
                # 其他情况low递增 缩小查找范围
                low = low + 1
            mid = int((high + low) / 2)
        return rotateArray[low]

```

