"""
Problem #1 Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Examples:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""


def palindrome(s):
    if len(s) <= 1: 
        return True
    if s[0] != s[-1]: 
        return False
    return palindrome(s[1:len(s)-1])

def convert(s):
    s = s.replace(" ", "").lower()
    new_str = []
    for i in s:
        if i.isalnum():
            new_str.append(i)
    
    s =  "".join(new_str)
    return palindrome(s)
        
print(convert("A man, a plan, a canal: Panama"))    
