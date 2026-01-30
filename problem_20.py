# Problem 20: Find common elements in two lists
# Find and fix the error

list1 = list(map(int, input("Enter elements of first list separated by spaces: ").split()))
list2 = list(map(int, input("Enter elements of second list separated by spaces: ").split()))
common = []
for item in list1:
    if item in list2 and item not in common:
        common.append(item)

print(f"Common elements: {common}")
