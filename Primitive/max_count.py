def solution(array: list) -> int:
  seen = {}

  for num in array:
    if num not in seen:
      seen[num] = 1
    else:
      seen[num] += 1
      
  max_count = max(seen, key=seen.get)
  return max_count
  
if __name__ == "__main__":
    nums = [4,4,4,5,5]
    print(solution(nums))
    nums = [2,2,1,1,1,2,2]
    print(solution(nums))

    
