# Problem: Find maximum element in an array
# Approach: Linear traversal
# Time Complexity: O(n)
# Space Complexity: O(1)
# Explanation:
# We start by assuming the first element is maximum,
# then compare it with every other element and update if needed.

arr = [10,4,12,33,15,54]
max = arr[i]

for i in range(len(arr)):
  if(arr[i] > max):
    max = arr[0]

print("maximum element is:",max)
