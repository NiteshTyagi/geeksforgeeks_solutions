def ascendingorder_selection(temp=[]):
    size = len(temp)
    for i in range(size):
        minimum = i
        for j in range(i+1,size):
            if temp[minimum]>temp[j]:
                minimum = j
        temp[i],temp[minimum] = temp[minimum],temp[i]
    return temp

def descendingorder_selection(dtemp = []):
    size  = len(dtemp)
    for i in range(size):
        maximum = i
        for j in range(i+1,size):
            if dtemp[maximum]<dtemp[j]:
                maximum = j
        dtemp[i],dtemp[maximum]=dtemp[maximum],dtemp[i]
    return dtemp

if __name__ == '__main__':
    # https://www.geeksforgeeks.org/selection-sort/
    arr = list(map(int,input('Enter the List of integers. e.g--> 5,1,6,2\n').split(',')))
    # temp = arr
    asc_arr = ascendingorder_selection(temp = arr)
    print('---- Ascending order Sorted Array ----- ',asc_arr)
    des_arr = descendingorder_selection(dtemp = arr)
    print('---- Descending order Sorted Array ----- ',des_arr)