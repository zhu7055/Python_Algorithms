#使用Divide and Conquer
#將未排序的陣列分為兩個子陣列,大小是原始陣列的一半。
#只要陣列的目前部分有多個元素,就繼續劃分子陣列。
#透過始終將最低值放在第一位,將兩個子數組合併在一起。
#繼續合併,直到沒有子數組為止。
def MergeSort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2#中間值
    left=arr[:mid]#左側資料
    right=arr[mid:]#右側資料

    sorted_left=MergeSort(left)#已排序左側
    sorted_right=MergeSort(right)#已排序右側

    return merge(sorted_left,sorted_right)
#merge
def merge(left,right):
    result=[]
    i=j=0
#在範圍內
    while i<len(left) and j<len(right):
        if left[i]<right[j]: #左邊小於右邊
            result.append(left[i])#新增到left
            i+=1
        else:
            result.append(right[j])#否則新增到right
            j+=1
    result.extend(left[i:]) #連接列表到result的後面
    result.extend(right[j:])#連接列表到result的後面

    return result
#main function to test the merge_sort function
if __name__=="__main__":
    UnsortedArr=[100,20,13,19,7,2,5,60]
    n=len(UnsortedArr)
    print(f"Unsorted Array:",UnsortedArr)
    #for i in range(n):
    #   print(f"{UnsortedArr[i]}",end=" ")

    SortedArr=MergeSort(UnsortedArr)
    print("Sorted Array(merge_sort):",SortedArr)
