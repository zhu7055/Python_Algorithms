def binary_search(arr:list[int],target:int,low:int,high:int)->int:
    # 二分搜尋：在已排序陣列 arr 中尋找 target，搜尋範圍為 low 到 high
    if low<=high:
        middle=(low+high)//2 # 取得中間索引
        if arr[middle]==target:# if中間值等於目標
            return middle      # 回傳index
        elif arr[middle]<target: # 若中間值小於目標
            return binary_search(arr,target,middle+1,high) # 往右半部遞迴搜尋
        else:
            return binary_search(arr,target,low,middle-1) # 往左半部遞迴搜尋
    else:
        return -1
#main function to test the binary_search function
if __name__=="__main__":
    arr=[1,7,13,15,20,50]
    target=15 #target:要搜尋的目標
    print("Binary Search")
    result=binary_search(sorted(arr),target,0,len(arr)-1) #執行二分搜尋
    if result!=-1:
        print(f"Found element at index {result}") # 找到則輸出索引
    else:
        print("Not found")