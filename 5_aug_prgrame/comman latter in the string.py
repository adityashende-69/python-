def comman_letters():

    s1 = input("enter a string")
    s2 = input("enter a string")
    
    s3 = set(s1)
    s4 = set(s2)


    list1 =  s3 & s4
    print(list1) 

comman_letters()
