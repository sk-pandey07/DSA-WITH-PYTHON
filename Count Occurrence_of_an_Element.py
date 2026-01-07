# Problem: Count frequency of an element in an array
# Approach: Linear traversal
# Time Complexity: O(n)
# Space Complexity: O(1)
# Explanation:
# We traverse the array once and compare each element with the target.
# Each time a match is found, the counter is incremented

n = int(input("enter number:"))
arr = []
for i in range(n):
  arr.append(int(input()))

x = int(input("select element:"))
count = 0
for i in range(n):
  if(arr[i] == x):
    count += 1

print("count=",count)
