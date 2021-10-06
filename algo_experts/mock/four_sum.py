#TODO

def find_array_quadruplet(arr, s):
  arr.sort()
  
  
  for p1 in range(0, len(arr)-3):
    for p2 in range(p1+1, len(arr)-4):
      p3 = p2+1
      p4 = len(arr) - 1
      while p3 < p4:
        if arr[p1] + arr[p2] + arr[p3] + arr[p4] == s:
          return [arr[p1], arr[p2], arr[p3], arr[p4]]

        elif arr[p1] + arr[p2] + arr[p3] + arr[p4] > s:
          p4 -= 1

        elif arr[p1] + arr[p2] + arr[p3] + arr[p4] < s: # right
          p3 += 1  
  
  return []

  