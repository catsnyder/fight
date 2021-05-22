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
        time.sleep (1)
        print ("the ingrate pauses. <i-i have something to tell you>, he begins.")
        time.sleep (1)
        print ("what is your next course of action? 1. let him continue 2. <as if i care to hear anything from the likes of you!!>")
        response = input ("1 or 2")
        if response == "1":
            print ("the scum turns away and blushes. <i-i really like you..>")
            time.sleep (1)
            print ("whaaaat? <but i dont even know you??>")
            time.sleep (1)
            print ("he turns back and smiles. <i've been following you for some time now...and i know you're the one for me!! you, love me too, dont you???>")
            time.sleep (2)
            print ("how will you respond? 1. <what?? no! get away, creep!> 2. <well....i guess we could go out sometime.>")
            response = input ("1 or 2")
            if response == "1":
                print ("you idiot!! he's a yandere! the yandere looks at you, shocked. <fine then...if i cant have you, no one can.> with that, he stabs you and you die.")
                time.sleep (1)
                print ("wow, you lost, idiot.")
                continue
            if response == "2":
                print ("the fiend smiles and blushes. looks like you got a date, i guess. congrats, you won this dumb game.")
        if response == "2":
            print ("the scum sheds tears of rage as he reels back, while a colorful bckground sequence ensues to illustrate his sheer power.")
            time.sleep (1)
            print ("in response, you also yell, triggering a background sequence of your own in a contrasting color.")
            time.sleep (1)
            print ("you realize as he pulls his fist back that you are unmatched to his sheer power. you close your eyes and await death. but wait...you arent dead yet? you look up and see the villian is...blushing???? oh no - he's a tsundere!")
            time.sleep (2)
            print ("<n-nevermind!> he blushes and runs away. i guess you got rid of him, for now. congrats, you won this dumb game.")
    time.sleep (3)    
    if response == "2":
        print ("ew! loser! try harder next time.")
        time.sleep (1)
        continue