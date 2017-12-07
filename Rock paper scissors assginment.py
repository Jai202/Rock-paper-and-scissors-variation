from random import *

################################################
#Objects: Hail, Rain, Snow, Wind, Sunr
################################################

    ## Hail is cooler than rain because it is colder
    ## Hail has more action going on compared to sun

    ## Rain is more wet which makes it better than wind
    ## Rain is warmer compared to snow which makes it better
    
    ## Snow doesn't hurt whereas hail does
    ## I don't think you can play with wind but you can play with snow
    
    ## Wind cools you down but sun warms you up 
    ## Wind blows the hail out of the way 
    
    ## Sun drys up all the water and get rids of rain
    ## Sun melts all the snow

gameOptions = ["Hail", "Rain", "Snow", "Wind", "Sun"]
print("This game is a variation of Rock, Paper and Scissors!")
print("Instead, this game has 5 options instead of 3!")
print("Here are the choices!")
print("Hail(H), Rain(R), Snow(Sn), Wind(W), and Sun(Su)!")
print("")

timetoplay = int(input("How many times will you like to play? "))
print("")
print("Sounds good!")
print("Lets play!")
print("")

playerScore = 0
computerScore = 0

for x in range(timetoplay):
    playersChoices = input("What will your choice be? ")
    print("")
    computerChoice = choice(gameOptions)


    while playersChoices not in ["H", "h", "R", "r", "Sn", "sn", "W", "w", "Su", "su"]:
        print("Sorry, this is not a vaild answer!")
        print("")
        playerChoices = input("What will you choose? ")
        
    if playersChoices in ["H","h"] and computerChoice == "Rain":
        computerChoice = print("The computers choice was", computerChoice, "!")
        print("Good Job!, you win!")
        playerScore = playerScore + 1
        print("Your score is now", playerScore)
        print("")
                                 
    elif playersChoices in ["H", "h"] and computerChoice == "Sun":
        computerChoice = print("The computers choice was", computerChoice,"!")
        print("Good job!, you win!")
        playerScore = playerScore + 1
        print("Your score is now", playerScore, "")

    elif playersChoices in ["R", "r"] and computerChoice == "Wind":
         computerChoice = print("The computers choice was", computerChoice, "!")
         print("Good job!, you win!")
         playerScore = playerScore + 1
         print("Your score is now", playerScore, "")

    elif playersChoices in ["R", "r"] and computerChoice == "Snow":
         computerChoice = print("The computers choice was", computerChoice, "!")
         print("Good job!, you win!")
         playerScore = playerScore + 1
         print("Your score is now", playerScore,"!")


    elif playersChoices in ["Sn", "SN", "sn"] and computerChoice == "Hail":
         computerChoice = print("The computers choice was", computerChoice, "!")
         print("Good job!, you win!")
         playerScore = playerScore + 1
         print("Your score is now", playerScore, "!")

    elif playersChoices in ["Sn", "SN", "sn"] and computerChoice == "Wind":
         computerChoice = print("The computers choice was", computerChoice, "!")
         print("Good job!, you win!")
         playerScore = playerScore + 1
         print("Your score is now", playerScore, "!")


    elif playersChoices in ["W", "w"] and computerChoice == "Sun":
         computerChoice = print("The computers choice was", computerChoice, "!")
         print("Good job!, you win!")
         playerScore = playerScore + 1
         print("Your score is now", playerScore, "!")

    elif playersChoices in ["W", "w"] and computerChoice == "Hail":
         computerChoice = print("The computers choice was", computerChoice, "!")
         print("Good job!, you win!")
         playerScore = playerScore + 1
         print("Your score is now", playerScore, "!")


    elif playersChoices in ["SU", "Su", "su"] and computerChoice == "Rain":
         computerChoice = print("The computers choice was", computerChoice, "!")
         print("Good job!, you win!")
         playerScore = playerScore + 1
         print("")
         print("Your score is now", playerScore, "!")

    else:
         playersChoices in ["SU", "Su", "su"] and computerChoice == "Snow"
         computerChoice = print("The computers choice was", computerChoice, "!")
         print("Good job!, you win!")
         playerScore = playerScore + 1
         print("Your score is now", playerScore, "!")

 
    

print("")
print ("       Game Summary")
print ("Player score        =   ", playerScore)
print ("Computer score      =   ", computerScore)
print ("Thanks for playing!")


