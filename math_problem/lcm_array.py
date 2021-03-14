from lcm import CalLCM

def Cal_LCM(array) -> int:
    if len(array)>=2:
        result = CalLCM(array[0],array[1])
        for num in array[2:]:
            result = CalLCM(result,num)
        return result
    else:
        return "Please Give at least 2 numbers."

if __name__ == '__main__':
    # https://www.geeksforgeeks.org/lcm-of-given-array-elements/

    array = list(map(int,input('Enter the number with space separated:\n').split(' ')))

    print(Cal_LCM(array))