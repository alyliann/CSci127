myString = input("Please enter a string: ")

for c in myString:
    print(c, ord(c)+1, chr(ord(c)+1))
