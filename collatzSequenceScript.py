# A program that explores the Collantz Sequence

userNumber = int(input('Please enter a number: '))


def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
        return number
    else:
        number = 3 * number + 1
        print(number)
        return number


for num in range(userNumber):
    print('userNumber: ', userNumber)
    if userNumber == 1:
        print('Collatz Sequence complete.')
        break
    else:
        userNumber = collatz(userNumber)
