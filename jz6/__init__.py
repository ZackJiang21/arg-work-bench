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
                return rotateArray[low]
            if rotateArray[low] < rotateArray[mid]:
                # mid处在前区间，low上移
                low = mid + 1
            elif rotateArray[mid] < rotateArray[high]:
                # mid在后区间，high下移
                high = mid
            else:
                low = low + 1
            mid = int((high + low) / 2)
        return rotateArray[low]
