def InsertionSort(arr):
    n=len(arr) #length of array
    if n<=1:
        return
    for i in range(1,n):
        key=arr[i]#當前元素insert到正確的位置
        j=i-1
        while j >= 0 and key < arr[j]:#在arr list範圍內
            arr[j+1]=arr[j]#大於key位置的元素，移動
            j-=1
        arr[j+1]=key #insertion key到正確的位置

arr=[20,15,10,30,7,6,5]
print(f"Unsorted List:{arr}")
InsertionSort(arr)
print(f"Sorted List:{arr}")
