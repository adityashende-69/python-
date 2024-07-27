num = [2,3,3,2,5,6,5,7,8,8]
numd =[]
for item in num:
    if item not in numd:
        numd.append(item)
print(numd)
