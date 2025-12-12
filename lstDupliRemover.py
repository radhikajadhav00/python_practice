items = [1, 3, 5, 3, 7, 1, 9, 5]

unique_items = []
for i in items:
    if i not in unique_items:
        unique_items.append(i)

print("Original list:", items)
print("Without duplicates:", unique_items)
