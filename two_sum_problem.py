# Problem: Find two numbers that add up to a target
# Approach: Brute force using nested loops
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Explanation:
# We check every possible pair of elements.
# If their sum equals the target, we print their indexes

arr = [2, 7, 11, 15]
target = 9
n = len(arr)

found = False

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == target:
            print("Indexes =", i, ",", j)
            found = True
            break
    if found:
        break

if not found:
    print("No pair found")
