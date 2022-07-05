"""
Implement a method to find the number of occurrences of any given word in a book. A word is represented as a string and a book is represented as an array / list of strings.

Optimize the method to be called multiple times.

Examples:

Input: ["The", "dog", "jumped", "in", "the", "dog", "house"], "dog"
Output: 2
"""

def solution(book, word):
  
  #check edge case
  if word is None or book is None:
    return -1

  #create counter
  count = 0

  for s in book:
    s.lower()
    if s == word.lower():
      count += 1
  
  return count
print(solution(["The", "dog", "jumped", "in", "the", "dog", "house"], "dog"))
