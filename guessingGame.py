import random
number= random.randint(1,9)

chances = 0
print(number)

while chances<3:
    guess = int(input('Enter your guess'))

    if guess == number:
        print('YOU WON')
        break

    elif guess< number:
        print('Your guess was low guess a higher number')
    else :
        print('Your guess was high guess a lower number')    

    chances=chances+1    

if not chances<3:
    print('YOU LOSE')
