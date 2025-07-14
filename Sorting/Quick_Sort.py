#1.具有要排序的值的數組。
#2.一個 QuickSort 如果子數組的大小大於 1,則呼叫自身（遞歸）的方法。
#3.一個 partition 接收子數組、移動值、將樞紐元素交換到子數組中並傳回子數組中下一次分割發生的索引的方法。

#1.選擇數組中的一個值作為樞紐元素。
#2.對數組的其餘部分進行排序,使得比樞軸元素更低的值位於左側,更高的值位於右側。
#3.將樞紐元件與較高值的第一個元件交換,使得樞軸元件落在較低值和較高值之間。
#4.對樞紐元件左側和右側的子陣列執行相同的操作（遞歸）。

def partition(arr,low,high):
    pivot=arr[high] #設定更大的元素為pointer(指針)
    i=low-1 #index 0
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            (arr[i],arr[j])=(arr[j],arr[i]) #小於等於pivot，移到左邊
    (arr[i+1],arr[high])=(arr[high],arr[i+1])#大於pivot的，移到右邊
    return i+1

def QuickSort(arr,low,high):#遞迴排序，對基準點的左右兩邊的子數列重複選擇基準點和partition
    if low<high:
        pivot_index=partition(arr,low,high)
        QuickSort(arr,low,pivot_index-1)
        QuickSort(arr,pivot_index+1,high)
#直到每個子數列只剩一個元素或為空，sort完成

new_array=[-2,10,7,5,9,13,20]

print(f"Unsorted Array:{new_array}")
QuickSort(new_array,0,(len(new_array))-1)
print(f"Sorted Array:{new_array}")