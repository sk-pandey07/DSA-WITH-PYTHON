# Problem: Move all zero elements to the end of the array
# Approach: Two-pointer / overwrite technique
# Time Complexity: O(n)
# Space Complexity: O(1)
# Explanation:
# We move all non-zero elements to the front of the array
# while maintaining their order Then, we fill the remaining
# positions with zeros

n = int(input("enter number:"))
arr = []
for i in range(n):
  arr.append(int(input()))

k = 0
for i in range(n):
  if(arr[i] != 0):
    arr[k] = arr[i]
    k += 1

for i in range(k,n):
  arr[i] = 0

print("move all zero element to the end:",arr)
