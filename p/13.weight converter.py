weigth = int(input('enter your wiigth: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == 'L':
  converter =  weigth * 0.45
  print( f'you are{converter} kilos ')
else:
   converter =  weigth / 0.45
   print(f'you are {converter} pounds ')