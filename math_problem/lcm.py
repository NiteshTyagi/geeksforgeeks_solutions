def CalLCM(num1:int,num2:int) -> int:
    large = max(num1,num2)
    small = min(num1,num2)
    
    i=large
    while 1:
        if (i%small==0):
            return i
        i+=large


def Cal_Lcm_PrimeFactor(num1:int,num2:int) -> int:
    from collections import Counter
    num1 = Counter(PrimeFactor(num1))
    num2 = Counter(PrimeFactor(num2))
    
    result = 1
    for k,v in num1.items():
        if k in num2:
            result*= (k**max(num1[k],num2[k]))
            del num2[k]
        else:
            result*=(k**num1[k])
    
    for k,v in num2.items():
        result*=(k**num2[k])

    return result


def PrimeFactor(num:int):
    i=2
    result = []
    while num>1:
        if num%i==0:
            result.append(i)
            num//=i
        else:
            i+=1
    return result


if __name__ =='__main__':
    ''' LCM Can be Found by three methods:
        1.By Prime Factor.
        2.By listing all multiple of numbers and find the common one.
        3.By using relation between GCD and LCM.
    '''
    num1 = int(input('Enter the First Number:'))
    num2 = int(input('Enter the Second Number:'))

    # LCM without GCD
    print(CalLCM(num1,num2))

    # LCM with Prime Factor
    print(Cal_Lcm_PrimeFactor(num1,num2))