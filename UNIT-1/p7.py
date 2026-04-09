# Given Lists
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print("Original list1:", list1)
print("Original list2:", list2)

# i. List Concatenation
concat_list = list1 + list2
print("\nConcatenated List:", concat_list)

# ii. Remove list1[3]
list1.pop(3)
print("After removing list1[3]:", list1)

# iii. Add "Java" in list1
list1.append("Java")
print("After adding 'Java':", list1)

# iv. Update list2 as list2[3] = 11
list2[3] = 11
print("After updating list2[3]=11:", list2)

# v. del list2[2]
del list2[2]
print("After deleting list2[2]:", list2)

# vi. Print message 4 times
for i in range(4):
    print("Welcome to Marwadi University")

# vii. Slicing operations
print("\nlist1[-2]:", list1[-2])
print("list2[1:3]:", list2[1:3])
print("list1[-1:-3]:", list1[-1:-3])   # returns empty list

# viii. Length of list2
print("\nLength of list2:", len(list2))

# ix. Maximum element in list1
# (Only numeric elements)
numeric_elements = [x for x in list1 if isinstance(x, int)]
if numeric_elements:
    print("Maximum numeric element in list1:", max(numeric_elements))
else:
    print("No numeric element found in list1")

# x. Minimum element in list2
print("Minimum element in list2:", min(list2))

# xi. list2.append(100)
list2.append(100)
print("After appending 100:", list2)

# xii. Extend operation
list2.extend([200, 300])
print("After extend operation:", list2)

# xiv. Difference between pop() and remove()
temp_list = [10, 20, 30, 20]
print("\nOriginal temp_list:", temp_list)

temp_list.pop(1)          # removes by index
print("After pop(1):", temp_list)

temp_list.remove(20)      # removes by value
print("After remove(20):", temp_list)

# xv. Reverse list1
list1.reverse()
print("\nAfter reverse list1:", list1)

# xvi. Sort list2 in descending order
list2.sort(reverse=True)
print("list2 in descending order:", list2)
