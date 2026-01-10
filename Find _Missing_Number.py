# Problem: Find the missing number in an array
# Approach: Sum formula method
# Time Complexity: O(n)
# Space Complexity: O(1)
# Explanation:
# We calculate the expected sum of numbers from 1 to n.
# Then we subtract the actual sum of array elements.
# The difference gives the missing number

n = int(input("enter number:"))
arr = []
for i in range(n-1):
    arr.append(int(input()))

total_sum = n * (n + 1) // 2
arr_sum = 0

for i in range(n-1):
    arr_sum += arr[i]

missing = total_sum - arr_sum
print("missing value=",missing)
