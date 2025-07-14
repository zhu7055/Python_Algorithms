def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1


arr=[1,7,13,15,20,50]
target=15
result=linear_search(arr,target)
if result!=-1:
    print(f"Element at index {result}")
else:
    print("Element not found.")