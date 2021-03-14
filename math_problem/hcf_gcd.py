from collections import Counter

def Cal_GCD(num1:int,num2:int) -> int:
    # Euclidean algorithm  Method
    if num1>=num2:
        l=num1
        s=num2
    else:
        l=num2
        s=num1
    
    if s==0:
        return l
    else:
        return Cal_GCD(s,l%s)


def Cal_GCD_Prime(num1,num2):
    '''
        Calculate GCD(HCF) by Prime Factorization of the method.
    '''
    num1 = PrimeFactor(num1)
    num2 = PrimeFactor(num2)
    result=1
    for k,v in num1.items():
        if k in num2:
            result*= (k**min(num2[k],num1[k]))
    
    return result


def PrimeFactor(num:int):
    '''
        Calculate Prime Factor of the Given number.
30    '''
    i=2
    result = []
    while num>1:
        if num%i==0:
            result.append(i)
            num//=i
        else:
            i+=1
    return Counter(result)


if __name__ =='__main__':
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))

    print(Cal_GCD(num1,num2))

    print(Cal_GCD_Prime(num1,num2))
