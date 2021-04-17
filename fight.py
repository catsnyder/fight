from sense_hat import SenseHat
import time
sense = SenseHat()

blue = (0,0,225)
yellow = (255,255,0)
red = (255,0,0)
while (1):
    print ("what a nice day...it would be a shame if a random delinquent chose to attack!")
    time.sleep (3)
    print ("ruh roh raggey! whats that?? a scoundrel!")
    time.sleep (1.5)
    print ("what do you do?  1. challenge him to a scrap 2. run away like a coward")
    time.sleep (1)
    response = input ("1 or 2 ")
    if response == "1":
        print ("excellent choice, old chap!")
        time.sleep (2)
        print ("the hooligan leers at you. <oho, you're approaching me?>")
        time.sleep (1)
        print ("how do you choose to attack? 1. rick roll him 2. insult his ancestry")
        time.sleep (1)
        response = input ("1 or 2 ")
        if response == "1":
            print ("the agressor is distracted and embarassed he fell for it. very effective!")
        if response == "2":
            print ("the agressor rolls his eyes; < sticks and stones may break my bones, but words will never hurt me! > ineffective.")
    time.sleep (3)    
    if response == "2":
        print ("ew! loser! try harder next time.")
        time.sleep (1)
        continue