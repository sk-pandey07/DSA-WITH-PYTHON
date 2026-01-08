# Problem: Find second largest element in an array
# Approach: Single traversal
# Time Complexity: O(n)
# Space Complexity: O(1)
# Explanation:
# We keep track of the largest and second largest elements.
# While traversing the array, we update them accordingly

n = int(input("enter number:"))
arr = []
for i in range(n):
  arr.append(int(input()))

largest = arr[0]
second_largest = -1

for i in range(1,n):
  if(arr[i] > largest):
    second_largest = largest
    largest = arr[i]
  elif(arr[i] < largest and arr[i] >second_largest):
    second_largest = arr[i]

print("second largest number is:",second_largest)
