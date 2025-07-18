def counting_sort(arr):
    max_val=max(arr)#find the maximum value in the array
    count=[0]*(max_val+1)#create a count array with size of max_val+1
    
    while len(arr)>0:#count the occurrences of each number
        num=arr.pop(0)#pop the first element
        count[num]+=1#increment the count for that number
    #reconstruct the sorted array
    for i in range(len(count)):
        while count[i]>0: #while there are occurrences of the number
            arr.append(i) #append the number to the sorted array
            count[i]-=1 #decrement the count for that number
    
    return arr
#main function to test the counting_sort function
if __name__=="__main__":
    arr=[5,2,9,1,7,6,17,3,4,8,10]
    print(f"Original array:{arr}")
    sorted_arr=counting_sort(arr)
    print(f"Sorted array(counting_sort):{sorted_arr}")