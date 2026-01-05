# Problem: Count even and odd elements in an array
# Approach: Linear traversal
# Time Complexity: O(n)
# Space Complexity: O(1)
# Explanation:
# We traverse the array once and check each element.
# If the element is divisible by 2, it is even; otherwise, it is odd.
# We maintain two counters to keep track of even and odd elements.

arr = [1,2,3,4,5,6]
even = 0
odd = 0

for i in range(len(arr)):
  if(arr[i] % 2 == 0):
    even += 1
  else:
    odd += 1

print("total even number is:",even)
print("total odd number is:",odd)
