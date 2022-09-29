#Name: Alysa Liann Vega
#Email: alysa.vega72@myhunter.cuny.edu
#Date: September 28, 2021
#This program assigns influencer tiers based on follower count

followers = int(input("Enter amount of social media followers: "))

if followers < 0:
    print("Your influencer tier is: Error")
elif followers < 1000:
    print("Your influencer tier is: Hyper Influencer")
elif followers < 10000:
    print("Your influencer tier is: Nano Influencer")
elif followers < 100000:
    print("Your influencer tier is: Micro Influencer")
elif followers < 500000:
    print("Your influencer tier is: Mid-Tier Influencer")
elif followers < 1000000:
    print("Your influencer tier is: Macro Influencer")
elif followers > 1000000:
    print("Your influencer tier is: Celebrity Influencer")
