#if you don't know how to play blackjack, tbh not super important but look it up anyway LOL
#this script is going to require some googling: I want you to practice using your resources with this one. But of course if you get stuck, reach out :)
'''instructions: randomly generate three values between 1 and 11. in the function bust: add these three numbers together. if they add up to or less than 21, return the sum. If it's over 21, return 0. If it's over 21 BUT there's an 11 as one of the values, return the sum - 10. '''
import random
def bust(num1,num2,num3):

    cards= (num1+num2+num3)
    if cards <= 21:
        return(num1+num2+num3)
    elif cards > 21 and num1==11 or num2==11 or num3== 11:
        return(10)
    else:
        return(0)

def main():

    num1 = random.randint(1, 11)
    num2 = random.randint(1, 11)
    num3 = random.randint(1, 11)
    print("Your numbers are:", num1,num2,num3)

    total = bust(num1, num2, num3)
    if total == 0:
        print("Bust!")
        print("Sorry you went over 21")
    elif total == 10:
        print("You went over 21 but had an 11")
        print("Your hand is 10")
    else:
        print("Your hand is", bust(num1, num2, num3))

main()