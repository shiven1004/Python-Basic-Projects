board={'7':' ','8':' ','9':' ',
       '4':' ','5':' ','6':' ',
       '1':' ','2':' ','3':' '}


def printBoard(board):
    print(board['7']+'|'+board['8']+'|'+board['9'])
    print('-+-+-')
    print(board['4']+'|'+board['5']+'|'+board['6'])
    print('-+-+-')
    print(board['1']+'|'+board['2']+'|'+board['3'])



def play():

    turn='X'
    count=0

    for i in range(9):
        printBoard(board)
        print("It's your turn,"+turn+".Input the place...")

        move=input()

        if board[move]==' ':
            board[move]=turn
            count+=1
        else:
            print("Place is filled!!Try Again!!!")
            continue

        if count>=5:
            if board['7'] == board['8'] == board['9'] != ' ': 
                printBoard(board)
                print("Game Over.")                
                print(turn + " won.")                
                break
            elif board['4'] == board['5'] == board['6'] != ' ': 
                printBoard(board)
                print("Game Over.")                
                print(turn + " won.")
                break
            elif board['1'] == board['2'] == board['3'] != ' ': 
                printBoard(board)
                print("Game Over.")                
                print(turn + " won")
                break
            elif board['1'] == board['4'] == board['7'] != ' ': 
                printBoard(board)
                print("Game Over.")                
                print(turn + " won.")
                break
            elif board['2'] == board['5'] == board['8'] != ' ': 
                printBoard(board)
                print("Game Over.")                
                print(turn + " won. ")
                break
            elif board['3'] == board['6'] == board['9'] != ' ': 
                printBoard(board)
                print("Game Over.")                
                print(turn + " won. ")
                break 
            elif board['7'] == board['5'] == board['3'] != ' ':
                printBoard(board)
                print("Game Over.")                
                print(turn + " won. ")
                break
            elif board['1'] == board['5'] == board['9'] != ' ': 
                printBoard(board)
                print("Game Over.")                
                print(turn + " won. ")
                break
        if count==9:
            print("It's a tie")


        if turn=='X':
            turn='O'
        else:
            turn='X'


play()                


board_keys=[]

for key in board:
    board_keys.append(key)


restart=input("Do you want to play again? (y/n)")
if restart=='y' or restart=='Y':
    for key in board_keys:
        board[key]=' '
    play()
elif restart=='n' or restart=='N':
    print("Thank You for playing...... Come again soon!!!")
