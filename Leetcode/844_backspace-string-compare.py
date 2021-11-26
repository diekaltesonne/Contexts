class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = []
        b = []
        for i in range(len(s)):
            if s[i] !='#':
                a.append(s[i])
            else:
                if len(a)!=0:
                    a.pop()
        for i in range(len(t)):
            if t[i] !='#':
                b.append(t[i])
            else:
                if len(b)!=0:
                    b.pop()
        return a == b