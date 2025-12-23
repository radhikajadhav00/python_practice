arr=[21,-5,12,45,23]
min_val=arr[0]
for i in arr[1:]:
    if i < min_val:
        min_val=i
print("minimun element is:",min_val)