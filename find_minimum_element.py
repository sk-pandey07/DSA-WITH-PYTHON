# Problem: Find minimum element in an array
# Approach: Linear traversal
# Time Complexity: O(n)
# Space Complexity: O(1)
# Explanation:
# We assume the first element as the minimum value and compare it
# with the remaining elements one by one. If a smaller value is found,
# we update the minimum variable.

arr = [4,3,2,8,1,6]
min = arr[0]

for i in range(len(arr)):
  if(arr[i] < min):
    min = arr[i]

print("minimum element of a array:",min)
