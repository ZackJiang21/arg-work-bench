# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        stack = []
        i = 0
        j = 0
        while i < len(pushV):
            if pushV[i] != popV[j]:
                stack.append(pushV[i])
                i = i + 1
            else:
                j = j + 1
                i = i + 1
                while len(stack) != 0 and popV[j] == stack[len(stack) - 1]:
                    stack.pop()
                    j = j + 1
        return len(stack) == 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.IsPopOrder([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
