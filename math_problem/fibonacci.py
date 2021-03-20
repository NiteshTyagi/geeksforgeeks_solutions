def recusive_fib(num: int):
    # Very bad approach for number >30
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return recusive_fib(num-1)+recusive_fib(num-2)


def dp_storeApproach(num: int):
    fib = [0]*(num+1)
    fib[0], fib[1] = 0, 1
    for i in range(2, num+1):
        fib[i] = fib[i-1]+fib[i-2]
    return fib[num]


def direct_formula(num: int):
    from math import sqrt
    result = round(pow((1+sqrt(5))/2, num)/(sqrt(5)))
    return result


def matrix_based(num):
    F = [[1, 1], [1, 0]]
    power(F, num-1)
    return F[0][0]


def multiple_matrix(F, M):
    x = (F[0][0] * M[0][0] +
         F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
         F[1][1] * M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w

def power(F, n):
    M = [[1, 1], [1, 0]]
    for i in range(2,n+1):
        multiple_matrix(F, M)


if __name__ == '__main__':
    # https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
    num = int(input('Enter the numbber: '))

    print('Fibonacci by recursion -->: ', recusive_fib(num))
    print('Fibonacci by DP approach to store whole series -->: ',
          dp_storeApproach(num))
    print('Fibonacci by Direct Formula approach -->: ', direct_formula(num))
    print('Fibonacci by Matrix based Formula approach -->: ', matrix_based(num))
