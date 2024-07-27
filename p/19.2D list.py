list = [
[1,2,3],
[2,3,4],
[7,8,9]
]
#print(list)

#print(list[0][2])
'''list[0][2] = 10
print(list)'''

for i in list:
    for row in i:
        print(row * 4)