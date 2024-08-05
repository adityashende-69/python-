import random 

try:
    def guessing_game():
        number = random.randint(1,10)
        guess = None
        attempts = 0



        while guess != number :
            guess = int(input("guess the number:"))
            attempts += 1

            if guess < number:
                print("to low")
            elif guess > number:
                print("to high")

            else:
                print(f'you guess right in  {attempts}')


    guessing_game()
except ValueError:
    print('enter integers only')