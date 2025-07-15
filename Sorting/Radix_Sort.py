#Step 1:求數組中最大的元素，902。有三位數字，因此迭代3次，每個位置一次
#Step 2:根據digit位數0對元素進行排序。使用最穩定的排序(counting sort)，對每個位置的數字進行排序。相同的key可能與input的數組順序不同。可以以相反的順序迭代輸入數組來建立output數組。
#對單位數字對數組進行counting sort。
#基於單位數字的排序數組為[170,60,902,2,13,24,35,76,67]
#Step 3:根據十位數字對元素進行排序。
#對十位數字進行counting sort
#基於十位數字的排序數組為[902,2,13,24,35,60,67,170,76]
#Step 4:根據百位數字對元素進行排序。
#根據百位數字對元素進行排序。
#基於百位數字的排序數組為[2,13,24,35,60,67,76,170,902]
#Counting Sort
def CountingSort(arr,exp1):
    n=len(arr)

    #output array elements that will have sorted arr
    output=[0]*(n)

    #初始化count array成0
    count=[0]*(10)

    #儲存count of 存在 in count[]
    for i in range(0,n):
        index = (arr[i]/exp1)
        count[int((index)%10)]+=1
    
    #更改 count[i] 以便 count[i] 現在包含該數字在輸出數組中的實際位置
    for i in range(1,10):
        count[i]+=count[i-1]

    #建立output array
    i=n-1
    while i>=0:
        index = (arr[i]/exp1)
        output[ count[int((index)%10)]-1]=arr[i]
        count[int((index)%10)]-=1
        i-=1
    #複製輸出數組 到 arr[],因此不包含排序的數字
    i=0
    for i in range(0,len(arr)):
        arr[i]=output[i]

#Radix Sort
def RadixSort(arr):

    #找出已知位數的最大數字
    max1=max(arr)

    #每個digit執行counting sort.請注意，這裡傳遞的是指數，而不是數字。指數等於 10^i。
    # 其中 i 是當前數字
    exp=1
    while max1//exp>0:
        CountingSort(arr,exp)
        exp*=10

if __name__=="__main__":
    arr=[170,60,902,2,13,24,35,76,67]
    print(f"Unsort List:{arr}")

    print("Sorted List:")
    RadixSort(arr)
    for i in range(len(arr)):
        print(arr[i],end=" ")
