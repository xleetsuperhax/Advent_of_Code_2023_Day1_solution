file = open('input.txt', 'r')

sumArray = []

for x in file:
    # Nested loop to check if the letter is a number or not
    firstNumber = None
    secondNumber = None
    for y in x:
        if(y.isdigit() and firstNumber is None):
            firstNumber = y
        elif(y.isdigit() and firstNumber is not None):
            secondNumber = y

    if(secondNumber is None):
        numberSum = str(firstNumber) +  str(firstNumber)
    else: 
        numberSum = str(firstNumber) + str(secondNumber)

    sumArray.append(int(numberSum))
    print(sumArray)

# add sums of array together
sumOfArray = 0
for x in sumArray:
    sumOfArray += x

print(sumOfArray)