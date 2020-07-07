places = {'1,1': '.', '1,2': '.', '1,3': '.',
          '2,1': '.', '2,2': '.', '2,3': '.',
          '3,1': '.', '3,2': '.', '3,3': '.'}


def printBoard(places):
    print(places['1,1'] + ' ' + places['1,2'] + ' ' + places['1,3'])
    print(places['2,1'] + ' ' + places['2,2'] + ' ' + places['2,3'])
    print(places['3,1'] + ' ' + places['3,2'] + ' ' + places['3,3'])


def match(places):
    printBoard(places)
    # players to switch between
    players = ['1', '2']
    # pieces to switch between
    pieces = ['X', 'O']
    # count so that I can check how many goes have happened
    count = 0
    # index that switches between player 1 and 2, pieces X and O
    index = 0

    # keep the loop running until someone has given a correct move or the amount of moves has run out
    while count < 9:
        # input for player to choose their position
        inputCoord = input(
            "\nPlayer " + players[index] + " enter a coord x,y to place your " + pieces[index] + " or enter 'q' to give up: ")
        # if the input is correct (its not an incorrect coordinate) check if the place is already filled. if it isnt, put the
        # piece there and break the loop, if it is, let the person have another try (continue the loop)
        if inputCoord in places:
            # check if the place is empty
            if places[inputCoord] == ".":
                # if its empty, put the piece there
                places[inputCoord] = pieces[index]
                # check if the piece placement has now resulted in a win
                won = checkForWin()
                # if you have won, end the game by breaking the loop
                if won == "yes":
                    print("\nMove accepted, well done you've won the game!")
                    printBoard(places)
                    break
                # if the piece placement didnt result in a win, show the board, change the player and piece and start again
                else:
                    print("\nMove accepted, here's the current board:\n")
                    printBoard(places)
                    # if the index is 0, 1 / 2 is 1 so the index will change to 1
                    # if the index is 1, 2 / 2 is 0 so the index will change to 0
                    index = (index+1) % len(players)
                    # if count has reached 8 (there have been 9 moves) then it is a draw as no one has won yet
                    if count == 8:
                        print("\nWe have reached a draw! Thank you for playing.")
                        break
                    count += 1
            else:
                print("\nOh no, a piece is already at this place! Try again...")
        #logic for quitting
        elif inputCoord == "q" or inputCoord == "Q":
            print("You have chosen to quit. Thank you for playing!")
            break
        #anything aside from the places and the letter q are considered incorrect input
        else:
            print("Incorrect input! Please enter the co-ordinates in the right format. For example '1,3'")


def checkForWin():
    won = "no"
    # checking for all possible combinations of winning, making sure there are no '.' in a winning row and that the pieces match
    if places['1,1'] == places['1,2'] == places['1,3'] != "." or\
            places['2,1'] == places['2,2'] == places['2,3'] != "." or\
            places['3,1'] == places['3,2'] == places['3,3'] != "." or\
            places['1,1'] == places['2,1'] == places['3,1'] != "." or\
            places['1,2'] == places['2,2'] == places['3,2'] != "." or\
            places['1,3'] == places['2,3'] == places['3,3'] != "." or\
            places['1,1'] == places['2,2'] == places['3,3'] != "." or\
            places['1,3'] == places['2,2'] == places['3,1'] != ".":
        # if one of these is true, they have won the game
        won = "yes"
    return won


print("\nWelcome to Tic Tac Toe!\n")
print("Here's the current board:\n")
match(places)
