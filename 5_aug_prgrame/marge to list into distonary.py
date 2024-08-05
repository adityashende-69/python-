def con_list_dic():
    l1 = [1,2,3]
    l2 = ["one" , "two" , "three"]
    result =dict(zip(l1 , l2))

    print(result)
con_list_dic()



def disc_tuple():
    d1 = {1 : "one" , 2 : "two" , 3 : "three"}
    for i in d1.items():
        print(i);


disc_tuple()