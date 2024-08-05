'''s = input("enter the string: ")
reverse = s[::-1]

if (s == reverse):
    print("this is a palindrome ")

else:
    print("this not a palindrome")'''



def palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
word = input('enter the sring:  ')
if palindrome(word):
    print('this is the palindrome: ')
else:
    print('this is not a palindrome: ') 
