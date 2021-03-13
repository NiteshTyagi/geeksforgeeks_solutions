def checkOppositeSign(num1,num2):
    return (num1^num2)<0

if __name__ == "__main__":
    # https://www.geeksforgeeks.org/detect-if-two-integers-have-opposite-signs/
    
    num1 = int(input('Enter Number1:'))
    num2 = int(input('Enter Number2:'))

    print(checkOppositeSign(num1,num2))