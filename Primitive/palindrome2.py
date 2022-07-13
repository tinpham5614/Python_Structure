"""

Input: s = "aba"
Output: true

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Input: s = "abc"
Output: false
"""

def palindrome(s):
    if len(s) <= 1: 
        return True
    if s[0] != s[-1]: 
        return False
    return palindrome(s[1:len(s)-1])
def convert(s):
    s = s.replace(s[-2], "").lower()
    new_str = []
    for i in s:
        if i.isalnum():
            new_str.append(i)
    
    s =  "".join(new_str)
    return palindrome(s)
print(convert("aba"))  
