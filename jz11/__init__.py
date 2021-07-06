# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        if n < 0:
            n = n & 0xffffffff
        print(bin(n))
        count = 0
        while n != 0:
            count = count + 1
            n = n & (n - 1)
            print(bin(n))
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.NumberOf1(-1))
