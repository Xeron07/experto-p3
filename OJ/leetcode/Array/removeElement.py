def remove_element(arr,val):
    repeat = 0
    inx = len(arr) - 1
    for i in range(0, len(arr)):
        if arr[i] != val:
            arr[repeat] = arr[i]
            repeat = repeat + 1

    return repeat

arr=[3,2,2,3]
print(remove_element(arr,2))