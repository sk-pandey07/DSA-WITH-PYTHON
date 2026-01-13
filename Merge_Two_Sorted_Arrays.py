# Problem: Merge two sorted arrays
# Approach: Two-pointer technique
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
# Explanation:
# We compare elements from both arrays and add the smaller one
# to the merged array, then move the pointer forward.

arr1 = [1, 3, 5]
arr2 = [2, 4, 6]

i = 0
j = 0
merged = []

while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        merged.append(arr1[i])
        i += 1
    else:
        merged.append(arr2[j])
        j += 1

while i < len(arr1):
    merged.append(arr1[i])
    i += 1

while j < len(arr2):
    merged.append(arr2[j])
    j += 1

print("Merged array:", merged)
