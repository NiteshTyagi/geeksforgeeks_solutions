def selection(arr):
    size = len(arr)
    for i in range(size):
        minimum = i
        for j in range(i+1,size):
            if arr[minimum]>arr[j]:
                minimum = j
        arr[i],arr[minimum] = arr[minimum],arr[i]
    return arr


if __name__ == '__main__':
    
    arr = list(map(int,input('Enter the List of integers. e.g--> 5,1,6,2\n').split(',')))
    arr = selection(arr)
    print('---- Sorted Array ----- ',arr)