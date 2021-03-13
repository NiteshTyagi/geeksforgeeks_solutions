def AddOne(n):
    m=1
    while n&m:
        n=n^m
        m = m<<1
    
    return n|m


if __name__ == "__main__":
    # https://www.geeksforgeeks.org/add-1-to-a-given-number/
    
    num1 = int(input('Enter Number1:'))

    print(AddOne(num1))