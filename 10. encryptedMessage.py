#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: September 20, 2021
#This program prints a coded message

import string

word = input("Enter a word: ")

code = ""                                       #creates empty string

for c in word:
    length = len(string.ascii_uppercase)        #len() finds length of string
    index = string.ascii_uppercase.find(c)
    if index + 13 > length:
        code += string.ascii_uppercase[(index + 13) - length]
    else:
        code += string.ascii_uppercase[index + 13]

print("Your word in code is", code)
