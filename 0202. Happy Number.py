class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        for _ in range(1000):
            lst = [*n]
            n = str(sum([int(i)**2 for i in lst]))
            if n=='1':
                return True
        return False
