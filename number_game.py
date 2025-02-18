import random
random_number = random.randint(1,20)


def number_game():
    if guess== random_number:
        print(' you guessed it correct!')
    elif guess> random_number:
        print('your guess is high')
    else:
        print('your guess is low')

attempt=3

while attempt>0:
    print(f'you have',attempt,'attempt left')
    guess=int(input('you have to guess a number between 1 to 20: '))
    
    if 1 < guess < 20:
        number_game()
    else:
        print('please, enter a number between 1 to 20')
    attempt -=1

print('actual input is', random_number)