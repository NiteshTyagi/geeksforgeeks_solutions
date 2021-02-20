def asc_bubbleSort(temp=[]):
    size = len(temp)
    for i in range(size):
        for j in range(size-i-1):
            if temp[j]>temp[j+1]:
                temp[j],temp[j+1]=temp[j+1],temp[j]
    return temp

def des_bubbleSort(temp=[]):
    size = len(temp)
    for i in range(size):
        for j in range(size-i-1):
            if temp[j]<temp[j+1]:
                temp[j],temp[j+1]=temp[j+1],temp[j]
    return temp

def op_asc_bubbleSort(temp=[]):
    size = len(temp)
    for i in range(size):
        swapped = False
        for j in range(size-i-1):
            if temp[j]>temp[j+1]:
                temp[j],temp[j+1]=temp[j+1],temp[j]
                swapped = True
        
        if not swapped:
            break
    return temp

if __name__ == '__main__':

    # https://www.geeksforgeeks.org/bubble-sort/

    arr = list(map(int,input('Enter the List of integers. e.g--> 5,1,6,2\n').split(',')))
    print('------ Original Array----- ',arr)
    
    asc_arr = asc_bubbleSort(temp=arr.copy())
    print('------ Sorted Array in Ascending Order----- ',asc_arr,arr)
    
    des_arr = des_bubbleSort(temp=arr.copy())
    print('------ Sorted Array in Descending Order----- ',des_arr)

    # OPTIMAL APPROACH (If ARRAY IS SORTED,THEN NO NEED TO PARSE THE ARRAY,JUST BREAK THE LOOP)
    op_asc_arr = op_asc_bubbleSort(temp=arr.copy())
    print('------ (OPTIMAL) Sorted Array in Ascending Order----- ',op_asc_arr)