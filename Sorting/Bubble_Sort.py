def Bubble_sort(arr):
    for n in range(len(arr)-1,0,-1):
        #初始化swapped成false
        swapped=False

        for i in range(n):
            if arr[i]>arr[i+1]:
                
                #交換元素位置，當左邊元素>右邊元素
                arr[i],arr[i+1]=arr[i+1],arr[i]
                #交換元素完成，標記為True
                swapped=True
        #如果swap未標記True，list已完成排序
        if not swapped:
            break
#main function to test the bubble_sort function
if __name__=="__main__":
    arr=[12,10,9,5,7,2,50,1]
    print(f"Unsorted list:{arr}")

    Bubble_sort(arr)
    print(f"Sorted list(bubble_sort):{arr}")