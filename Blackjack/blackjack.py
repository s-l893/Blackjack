import random
import blackjack_logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

should_continue = ""

#Function for the player drawing cards
def draw(player_sum, player_hand):

    random_add = random.randint(0,12)
    player_hand.append (cards[random_add])
    player_sum += cards[random_add]
    return player_sum, player_hand 

#Function for the computer drawing cards
def computer_draw(computer_sum, computer_hand):
    random_add = random.randint(0,12)
    computer_hand.append (cards[random_add])
    computer_sum += cards[random_add]
    return computer_sum, computer_hand

#Function for the player winning
def playerwin(hand,sum, computerhand, computersum):
        print ("You win!")
        print (f"Your final hand: {hand}, your final score is {sum}")
        print (f"Computer's final hand: {computerhand}, the computer's final score is {computersum}")
        return 

#Function for the computer winning
def computerwin(hand,sum, computerhand, computersum):
    print ("You lost.")
    print (f"Your final hand: {hand}, your final score is {sum}")
    print (f"Computer's final hand: {computerhand}, the computer's final score is {computersum}")
    return

#Function for the whole game
def blackjack():

    #Logo
    print (blackjack_logo.logo + "\n" * 2)

    #Variables
    randomp1 = random.randint (0,12)
    randomp2 = random.randint (0,12)
    randomc1 = random.randint (0,12)
    randomc2 = random.randint (0,12)
    playerhand = []
    playersum = 0
    computerhand = []
    computersum = 0
    playersum += cards[randomp1]
    playersum += cards[randomp2]
    computersum += cards[randomc1]
    computersum += cards [randomc2]
    playerhand.append (cards[randomp1])
    playerhand.append (cards[randomp2])
    computerhand.append(cards[randomc1])
    computerhand.append(cards[randomc2])


    #First turn
    if playersum == 21:
        playerwin (playerhand, playersum, computerhand, computersum)
        return
    print (f"Your cards: {playerhand}, current score: {playersum}")
    print (f"Computer's first card: {cards[randomc1]}")
    another_card = input("Type 'y' to get another card, type 'n' to pass: \n").lower()
    print ("\n" * 2)

    #Player wins right away
    if computersum > 21:
        playerwin (playerhand, playersum, computerhand, computersum)
        return
    
    #computer wins right away
    if playersum > 21: 
        computerwin(playerhand, playersum, computerhand, computersum)
        return
            
    #Additional draws
    while another_card == "y":
           
        playersum, playerhand = draw(playersum, playerhand)
        
        print (f"Your cards: {playerhand}, current score: {playersum}")
        print (f"Computer's first card: {cards[randomc1]}")

        #You go over 21 with ace in your hand
        if playersum > 21 and 11 in playerhand:
            location = playerhand.index(11)
            playerhand[location] = 1

        #Determines if you win or lose after taking additional draws
        if playersum >= 21: 
            print (f"\n\n\nYour final hand: {playerhand}, your final score is {playersum}")
            print (f"Computer's final hand: {computerhand}, the computer's final score is {computersum}")
            if playersum > 21: 
                print ("You went over. You lost.")
                return   
            elif playersum == 21:
                print ("You win!")
                return
        
        another_card = input("Type 'y' to get another card, type 'n' to pass: \n").lower()     
        print ("\n" * 2)

    #Computer's turn to draw
    if another_card == 'n':
        while computersum < 17:
            computersum, computerhand = computer_draw(computersum,computerhand)
    
    #Ace card logic for the computer
        if computersum > 21 and 11 in computerhand:
            location = computerhand.index(11)
            computerhand[location] = 1

        #Comparing the two final results
        #bust from computer
        if computersum > 21: 
            playerwin(sum = playersum, hand = playerhand, computersum = computersum, computerhand = computerhand)
            return
        
        #Determines if the computer draws again or not
        elif computersum >= 17:
            print (f"Your final hand: {playerhand}, your final score is {playersum}")
            print (f"Computer's final hand: {computerhand}, the computer's final score is {computersum}")
            #Determines the winner assuming that both parties didn't go past 21
            if 21 - computersum < 21 - playersum:
                print ("You lose.")
            elif 21 - playersum < 21 - computersum:
                print ("You win!")
        return

#continue the game  
should_continue = ""
#Ensures no wrong inputs
while should_continue not in ["y", "n"]:
    should_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n").lower()
    if should_continue == "y":
        blackjack()
    for should_continue in ['y','n']:
        print("\n" * 3)
        should_continue = input("Do you want to play another game of Blackjack? Type 'y' to continue or 'n' to stop:\n")
        if should_continue == 'y':
            print("\n" * 50)
            blackjack()
        elif should_continue == 'n':
            break

