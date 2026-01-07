# Problem: Linear Search in an array
# Approach: Sequential search using loop
# Time Complexity: O(n)
# Space Complexity: O(1)
# Explanation:
# We traverse the array from start to end and compare each element
# with the target value. If found, we return its index.

n = int(input("enter number:"))
arr = []
for i in range(n):
    arr.append(int(input()))

target = int(input("chose nuber:"))
index = -1

for i in range(n):
    if(arr[i] == target):
       index = i
       break

if(index != -1):
  print("element found index:",index)
else:
  print("element not found")
