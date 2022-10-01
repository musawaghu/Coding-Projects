from Question import *


def main():
    trivia_list = [Question("What is 3 + 2?", "4", "7", "6", "5", 4),
                   Question("What color is the sky?", "Red", "Blue", "Green", "Yellow", 2),
                   Question("How many continents are there?", "7", "2", "8", "9", 1),
                   Question("What is the capital of California?", "Irvine", "Fresno", "Sacramento", "Cypress", 3)]
    player1_score = 0
    player2_score = 0
    for i in trivia_list:
        print(i)
        answer_choice1 = int(input("Player 1, choose an answer: "))
        answer_choice2 = int(input("Player 2, choose an answer: "))
        if i.guess(answer_choice1):
            player1_score += 1
            print("Player 1 is correct!")
        elif i.guess(answer_choice2):
            player2_score += 1
            print("Player 2 is correct!")
        else:
            print("Both players got the question wrong!")
    print("This is Player 1's score: ", player1_score)
    print("This is Player 2's score: ", player2_score)


main()
