# Problem: Sum of elements in an array
# Approach: Iterative loop
# Time Complexity: O(n)
# Space Complexity: O(1)
# Explanation:
# We traverse the array once and keep adding each element to a variable.

arr = [1,2,3,4,5,6,7,8,9]
sum = 0

for i in range(len(arr)):
  sum = sum + arr[i]

print("total sum of array:",sum)
