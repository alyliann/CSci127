#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: September 20, 2021
#This program reverses a message and creates an acronym

s = input()

s_rev = s[::-1]

print("Reversed phrase: ", s_rev)

s_rev_up = s_rev.upper()

phrase = s_rev_up.split()

print("Last letters of reversed words: ", end='')
for word in phrase:
    print(word[-1], end='')      #end='' makes it so the next loop does not
                                 #create a new line

#
#another way to do it is:
#

s = input()

s_rev = s[::-1]

print("Reversed phrase: ", s_rev)

s_rev_up = s_rev.upper()

phrase = s_rev_up.split()

acronym = ""                    #create empty string

for word in phrase:
    acronym += word[-1]         #adds  last character of each word to the acronym

print("Last letters of reversed words: ", acronym)  #prints the acronym n stuff
