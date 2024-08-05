sentance  = "hi there i have gave you 55 adn 60.8 rs to you "
num = []
for i  in sentance.split():
    if  not i.isalpha():        #  isalpha is used to to print all the words in the string we used not mrthod to manupalet it 
        num.append(i)
print(num)