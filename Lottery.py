# Lottery Application
import random

MAX = 5
def lotteryNumber():
    lottery = []
    for i in range(0,MAX):
        randomNum = random.randint(1,9)
        lottery.append(randomNum)
    print("Here are the winning lottery numbers\n",lottery)
    return lottery

def userNumber():
    user = []
    for i in range(0,MAX):
        print("Number",i+1,": ")
        n = int(input())
        user.append(n)
    print("Here are your numbers\n",user)
    return user

def compare(lottery, user):
    if lottery == user:
        print("Congrats! You are the grand prize winner.")
    else:
        for i in range(0,MAX):
            if(lottery[i]==user[i]):
                print("Element",i,"match. It's value is:",user[i])

def main():
    lottery = lotteryNumber()

    user = userNumber()
    
    compare(lottery, user)

main()