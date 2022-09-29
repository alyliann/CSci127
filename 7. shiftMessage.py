#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: September 17, 2021
#This program shifts a message by 5 characters

myString = input("Enter a message: ")

for c in myString:
    print(c, "shifted by 5 characters is: ", chr(ord(c)+5))
