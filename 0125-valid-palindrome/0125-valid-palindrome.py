class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=""
        for i in s:
            if i.isalnum():
                t+=i
        return (t.lower()==t[::-1].lower())