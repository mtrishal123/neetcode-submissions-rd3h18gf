class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left, total = 0, 0
        ans, path = [], []
        self.back(n, left, total, ans, path)
        return ans
    def back(self, n , left, total, ans, path):
        if len(path) == n*2:
            ans.append(''.join(path[:]))
            return
        if left < n:
            path.append('(')
            self.back(n, left + 1, total + 1, ans, path)
            path.pop()
        if total - left < left:
            path.append(')')
            self.back(n, left, total + 1, ans, path)
            path.pop()
        
        
