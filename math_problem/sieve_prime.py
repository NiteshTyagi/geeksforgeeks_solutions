def sieve_eratosthenes(start,end):
    # Time complexity is O(n*log(log(n)))

    result = [[i,True] for i in range(end+1)]
    p=2
    while p*p<=end:
        if result[p][1]:
            for j in range(p*p,end+1,p):
                result[j][1]=False
        p+=1
    for i in range(start-1,end+1):
        if result[i][1]:
            print(result[i][0])

if __name__ == '__main__':
    # https://www.geeksforgeeks.org/sieve-of-eratosthenes/
    start = int(input('Enter the starting range of the number:'))
    end = int(input('Enter the Ending Number:'))

    sieve_eratosthenes(start,end)