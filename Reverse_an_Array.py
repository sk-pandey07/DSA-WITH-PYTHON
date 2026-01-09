# Problem: Reverse an array
# Approach: Reverse traversal using loop
# Time Complexity: O(n)
# Space Complexity: O(1)
# Explanation:
# We traverse the array from the last index to the first index
# and print elements in reverse order without using extra space.

n = int(input("enter number:"))
arr = []
for i in range(n):
  arr.append(int(input()))

for i in range(n-1,-1,-1):
  print(arr[i]," ")
