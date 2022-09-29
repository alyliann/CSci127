#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: September 21, 2021
#This program prints book titles alongside author initials

books = input("Enter a list of books and their authors:")

books_split = books.split('; ')

for x in range(len(books_split)):
    books_split[x] = books_split[x].split(' - ')

for x in range(len(books_split)):
    books_split[x][1] = books_split[x][1].split(' ')

for x in books_split:
    print(x[0], "by", x[1][0][0] + "." + x[1][1][0] + ".")
