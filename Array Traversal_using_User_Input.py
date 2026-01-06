# Problem: Take array input from user and display elements
# Approach: Iterative input and output using loop
# Time Complexity: O(n)
# Space Complexity: O(n)
# Explanation:
# First, we take the size of the array from the user.
# Then, we input elements one by one and store them in a list.
# Finally, we traverse the array and print each element.

n = int(input("enter size:"))
arr = []

print("enter element:")
for i in range(n):
  arr.append(int(input()))

print("array element:")
for i in range(n):
  print(arr[i]," ")
  
