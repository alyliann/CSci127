#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: October 26, 2021
#This program returns the Olympic world record for an event

def worldRecord(gender, event):
    time = 0.0
    if gender == "men":
        if event == 100:
            time += 9.63
        elif event == 200:
            time += 19.30
        elif event == 400:
            time += 43.03
        else:
            time = -1
    elif gender == "women":
        if event == 100:
            time += 10.62
        elif event == 200:
            time += 21.34
        elif event == 400:
            time += 48.25
        else:
            time = -1
    else:
        time = -1
    return(time)

def main():
     z = input("Enter the gender: ").lower()
     t = int(input("Enter the event distance: "))
     record = worldRecord(z,t)
     print("The world record for "+z+"'s "+ str(t) + " meters is", record, "seconds")

#Allow script to be run directly:
if __name__ == "__main__":
     main()
