'''
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

mismatch from the left -> 
traverse and we get a number that is less than the prev
no longer non-decreasing
mismatch when A[left + 1] < A[left]

mismatch from the right ->
no longer non-increasing
mismatch when A[right - 1] > A[right]

Input: [1, 2, 5, 3, 7, 10, 9, 12]
                 ^     ^
Why include 5 in the window?
- 3 should be less than 5
  (local minima)

Why include 9 in the window?
- 9 should be less than 10
                        (local maxima)

Do we include 2 in the window?
- Right position in the array

Do we need to check element 1?
- No because we already know 1 < 2

Output: 5
Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted

Input: [1, 3, 2, 0, -1, 7, 10]
           ^        ^
Output: 5

Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted
Match:
2 pointers approach
Plan:
Scan from left to right and find first element that’s out of order 
 - find left pointer

Scan from right to left and find first element that’s out of order
 - find right pointer

Find the local minimum and local maximum in that sub-array

Extend subarray on both ends to include any number bigger than the local minimum and smaller than the local maximum
'''

# Implement

def length_smallest_subarray(arr):

  if len(arr) <= 1:
    return 0

  # initialize variables
  left = 0
  right = len(arr) - 1

  # if array is already sorted...
  if left == right:
    return 0
  # Scan from left to right and find first element that’s out of order 
  while left < right and arr[left + 1] >= arr[left]:
    left += 1

  # Scan from right to left and find first element that’s out of order
  # mismatch: arr[right - 1] > arr[right]
  while right > 0 and arr[right - 1] <= arr[right]:
    right -= 1
    
  # Find the local minimum and local maximum in that sub-array
  local_max = arr[left]  # float("inf")
  local_min = arr[left]  # float("-inf") or -float("inf")
  
  for i in range(left, right + 1):
    # compare & update local_max & local_min
    local_max = max(local_max, arr[i])
    local_min = min(local_min, arr[i])    

  # Extend subarray on both ends to include any number bigger than the local minimum and smaller than the local maximum

  # extend towards the left
    
  while left > 0 and arr[left - 1] > local_min:
    left -= 1

  # extend towards the right
  while right < len(arr) - 1 and arr[right + 1] < local_max:
    right += 1

  return right - left + 1

print(length_smallest_subarray([1, 2, 5, 3, 7, 10, 9, 12]))  # 5
print(length_smallest_subarray([1, 3, 2, 0, -1, 7, 10]))     # 5
print(length_smallest_subarray([1, 2, 3]))  # 0
print(length_smallest_subarray([]))   # 0
print(length_smallest_subarray([3, 2, 1]))   # 3
print(length_smallest_subarray([1, 2, 3, -1, 9, 10,12]))   # 4 (edge case)
print(length_smallest_subarray([1, 2, 4, 6, 5, 3, 7, 8]))
