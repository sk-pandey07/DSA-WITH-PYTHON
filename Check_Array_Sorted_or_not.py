# Problem: Check whether an array is sorted in ascending order
# Approach: Single traversal comparison
# Time Complexity: O(n)
# Space Complexity: O(1)
# Explanation:
# We compare each element with the next one.
# If any element is greater than its next element,
# the array is not sorted

n = int(input("enter number:"))
arr = []

for i in range(n):
  arr.append(int(input()))

is_sorted = True

for i in range(n-1):
  if arr[i] > arr[i + 1]:
    is_sorted = False

if is_sorted:
  print("array is sorted")
else:
  print("array is not sorted")
