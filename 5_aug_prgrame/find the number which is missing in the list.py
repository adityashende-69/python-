a = [1,2,3,4,5,6,7,8,10]


def missing_number(a):
    n = a[-1]
    total =  n*(n+1)//2
    sum1 = sum(a)
    print(total - sum1)


missing_number(a)