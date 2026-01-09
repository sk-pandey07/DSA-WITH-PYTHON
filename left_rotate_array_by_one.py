# Problem: Left rotate an array by one position
# Approach: Shift elements to the left
# Time Complexity: O(n)
# Space Complexity: O(1)
# Explanation:
# We store the first element, shift all elements one position to the left,
# and then place the first element at the end

n = int(input("enter number:"))
arr = []
for i in range(n):
  arr.append(int(input()))

first = arr[0]

for i in range(n - 1):
  arr[i] = arr[i + 1]

arr[n - 1] = first
print(arr)
