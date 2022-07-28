"""
Input: image = [[1,1,1],
                [1,1,0],
                [1,0,1]]
                sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],
         [2,2,0],
         [2,0,1]]


Input: image = [[0,0,0],
                [0,0,0]],
                sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],
         [2,2,2]]

Time : O(N)
Space: O(1)
"""

def dfs(image, sr, sc, newColor, originalColor):
  # check if indices are in bound
  if sr >= 0 and sr < len(image) and sc >= 0 and sc < len(image[0]) and image[sr][sc] == originalColor:
    # change the color to the new color
    image[sr][sc] = newColor

    #we check surrounding elements left, right, bottom, top
    dfs(image, sr-1, sc, newColor, originalColor)
    dfs(image, sr+1, sc, newColor, originalColor)
    dfs(image, sr, sc-1, newColor, originalColor)
    dfs(image, sr, sc+1, newColor, originalColor)



def flood_fill(image, sr, sc, newColor):
  #handle edge cases

  #check if we need to change the color
  if image[sr][sc] == newColor:
    return image
  #store the starting color
  originalColor = image[sr][sc]
  #callback function dfs
  dfs(image, sr, sc, newColor, originalColor)

  return image



print(flood_fill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))
print(flood_fill([[0,0,0],[0,0,0]],0,0,2))
  
 
  
