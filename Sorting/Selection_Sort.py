def selection_sort(arr:list[int])->list[int]:
    n = len(arr)#get the length of the array
    for i in range(n):
        min_index = i #set minium index to current index
        for j in range(i+1, n):# 從未排序區域尋找最小值
            if arr[j] < arr[min_index]:#if  found a smaller element
                min_index = j #update the index of the minimum element
        arr[i], arr[min_index] = arr[min_index], arr[i]  #swap the found minimum element    return arr
    return arr
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print(f"Original array:{arr}")
    selection_sort(arr)
    print(f"Sorted array:{arr}")