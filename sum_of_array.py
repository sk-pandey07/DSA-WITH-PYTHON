# Problem: Sum of elements in an array
# Approach: Iterative loop
# Time Complexity: O(n)
# Space Complexity: O(1)
# Explanation:
# We traverse the array once and keep adding each element to a variable.

n = int(input("enter number:"))
arr = []
for i in range(n):
  arr.append(int(input()))

sum = 0
for i in range(n):
  sum += arr[i]

print("sum of array:",sum)
