class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i != len(s) and j != -1:
            if i >= j:
                return True
            if s[i].isalnum() == False:
                i = i + 1
                continue
            if s[j].isalnum() == False:
                j = j - 1 
                continue
            if s[i].lower() == s[j].lower():
                i = i + 1
                j = j - 1
            else:
                #print(i,j)
                #print(s[i],s[j])
                return False 
        return True