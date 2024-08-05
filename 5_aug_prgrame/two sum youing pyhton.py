arr = [1,2,3,4,5,6,7,8,9]
sum1  = 6

def twosum(arr , sum1 ):
    arr.sort()
    left  =  0 
    rigth = len(arr)-1
    while(left <= rigth):
        if (arr[left] + arr[rigth] > sum1):
            rigth = rigth - 1
        elif (arr[left] + arr[rigth] < sum1):
            left = left + 1
        elif (arr[left] + arr[rigth] == sum1):
            print("value of pair" , arr[left], "&",arr[rigth])
            rigth = rigth - 1
            left = left + 1




twosum(arr ,sum1)
