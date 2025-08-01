from typing import List
def linear_search(arr:list[int],target:int)->int:
    for i in range(len(arr)): # 線性搜尋：逐一檢查陣列中的每個元素是否等於目標值
        if arr[i]==target:    # 如果找到目標值
            return i          # 回傳該元素的index
    return -1
#main function to test the linear_search function
if __name__=="__main__":
    arr=[1,7,13,15,20,50]
    target=7                # 要搜尋的目標值
    print("Linear Search")
    result=linear_search(arr,target) # 執行線性搜尋
    if result!=-1:
        print(f"Element at index {result}") # 找到則輸出索引
    else:
        print("Element not found.")