#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: November 16, 2021
#This program loops from 100 down to 0 stepping by 25

ADDI $s0, $zero, 100 #set s0 to 100
ADDI $s1, $zero, 25 #set s1 to 25
AGAIN: SUB $s0, $s0, $s1 #subtract s1 from s0, store it in s0
BEQ $s0, $zero, DONE #when s0 equals zero, end loop
J AGAIN
DONE: #to break out of loop
