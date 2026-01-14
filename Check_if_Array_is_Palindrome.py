# Problem: Check if an array is a palindrome
# Approach: Two-pointer comparison
# Time Complexity: O(n)
# Space Complexity: O(1)
# Explanation:
# We compare elements from the start and end of the array.
# If all matching pairs are equal, the array is a palindrome

arr = [1,2,3,2,1]
is_palindrome = True
n = len(arr)

for i in range(n//2):
  if arr[i] != arr[n-i-1]:
    is_palindrome = False
    break

if is_palindrome:
  print("palindrome array")
else:
  print("not palindrome")
