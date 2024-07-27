'''i = 0
while (i < 5):
    i += 1
    print('*' * i)
    '''

#guess game 

securate_number =  6
guess_limit = 3
guess_count = 0

while (guess_count < guess_limit):
    count = int(input('guess the number '))

    guess_count += 1
    if count == securate_number :
        print('you win ! ')
        break
else:
    print('sorr worng guess')