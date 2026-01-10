# Problem: Remove duplicate elements from a sorted array
# Approach: Build a new list with unique elements
# Time Complexity: O(n)
# Space Complexity: O(n)
# Explanation:
# We keep the first element and then compare each element
# with the last added unique element. If it is different,
# we add it to the unique list

n = int(input("enter number:"))
arr = []
for i in range(n):
  arr.append(int(input()))

unique = [arr[0]]
for i in range(1,n):
  if (arr[i] != unique[-1]):
    unique.append(arr[i])

print("after remove duplicate value:")
print(unique)
