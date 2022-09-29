#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: September 28, 2021
#This program converts parsecs to light-years and vice-versa

text = """
"Please enter the conversion you want to do:
'a' for Light-Year to Parsec conversion
'b' for Parsec to Light-Year conversion
"""
print(text)
aORb = input("Your selection: ")

if aORb == 'a':
    LY = input("Please enter a number of light-years: ")
    num_LY = float(LY)
    LYtoP = num_LY/3.26156
    print(num_LY, "Light-Years is equal to", LYtoP)

elif aORb == 'b':
    P = input("Please enter a number of parsecs: ")
    num_P = float(P)
    PtoLY = num_P*3.26156
    print(num_P, "Parsecs is equal to", PtoLY)

else:
    print("Error: invalid selection")
