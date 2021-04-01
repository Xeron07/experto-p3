#binary search technique

def binary_search(arr,target):
    if(arr[0]==target):
        return 0
    elif arr[len(arr)-1]==target:
        return len(arr)-1
    else:
        return searchByPosition(0,len(arr),arr,target)

def searchByPosition(start,end,arr,target):
    if(start==end):
        return start
    mid=int((start+end)/2)
    if(arr[mid]==target):
        return mid
    if(target>arr[mid]):
        return searchByPosition(mid+1,len(arr),arr,target)
    else:
        return searchByPosition(start, mid, arr, target)


arr=[1,3,5,6]
print(binary_search(arr,0))

