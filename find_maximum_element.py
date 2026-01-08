# Problem: Find maximum element in an array
# Approach: Linear traversal
# Time Complexity: O(n)
# Space Complexity: O(1)
# Explanation:
# We start by assuming the first element is maximum,
# then compare it with every other element and update if needed.

n = int(input("enter number:")
arr = []
for i in range(n):
  arr.append(int(input()))
  
max = arr[i]

for i in range(len(arr)):
  if(arr[i] > max):
    max = arr[0]

print("maximum element is:",max)
