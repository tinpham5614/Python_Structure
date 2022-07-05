def lengthOfLongestSubstring(s: str) -> int:
  if len(s) == 0 :
    return 0
  seen = {}
  current = 0
  maxlen = 0
  for i, l in enumerate(s):
      if l in seen and seen[l] >= i - current:
          current = i - seen[l]
          seen[l] = i
      else:
          seen[l] = i
          current += 1
      maxlen = max(maxlen,current)
  return maxlen
print(lengthOfLongestSubstring("bbbbb"))
            
        
