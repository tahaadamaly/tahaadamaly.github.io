import random

# Roulette

red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

def spin(number=None, color=None, bet=None):
    pot = bet
    choice = random.randrange(0, 37, 1)
    winning_color = ''
    if choice in red:
        winning_color = 'red'
    elif choice in black:
        winning_color = 'black'
    else: 
        winning_color = 'green'

    print("Rolling...")
    print("Ball lands on: " + str(choice) + ", which is " + winning_color)

    if number==choice:
        print("Winning number!")
        pot = pot*35
        print("Total winnings: " + str(pot))
    if color=="red" and choice in red:
        print("Winning color!")
        pot = pot*2
        print("Total winnings: " + str(pot))
    if color=="black" and choice in black:
        print("Winning color!")
        pot = pot*2
        print("Total winnings: " + str(pot))


spin(number=0, color='red', bet=10)
