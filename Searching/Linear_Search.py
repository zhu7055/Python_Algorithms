from typing import List
def linear_search(arr:list[int],target:int)->int:
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
#main function to test the linear_search function
if __name__=="__main__":
    arr=[1,7,13,15,20,50]
    target=7
    print("Linear Search")
    result=linear_search(arr,target)
    if result!=-1:
        print(f"Element at index {result}")
    else:
        print("Element not found.")