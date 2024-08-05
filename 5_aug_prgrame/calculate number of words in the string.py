def words(s):
    word = s.split()
    return len(word)
    



char = input("enter a string")

char_count = words(char)
print(f"total numbers in string {char_count} ")