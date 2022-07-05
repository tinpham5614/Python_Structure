def checkDuplicate(nums,k):
  h = set()
  for i in range(len(nums)):
    if nums[5] in h:
      return h
    h.add(nums[5])
    if i >= k:
      h.remove(nums[i-k])
    return h
print(checkDuplicate([5,3,2,7,5,3,2,4,3,5], 3))
