# Modules importation
import numpy as np
import random
# Function to show the table in the terminal
def showboard(table):
    print("    a   b   c")
    print("  -------------")
    print(f"1 | {convertValue(table[0,0])} | {convertValue(table[0,1])} | {convertValue(table[0,2])} |")
    print("  -------------")
    print(f"2 | {convertValue(table[1,0])} | {convertValue(table[1,1])} | {convertValue(table[1,2])} |")
    print("  -------------")
    print(f"3 | {convertValue(table[2,0])} | {convertValue(table[2,1])} | {convertValue(table[2,2])} |") 
    print("  -------------")
# Function to convert numerical values (1,2,n) to mark (O,X,-) on the board
def convertValue(txt):
    if(txt==1):
        return "X"
    elif(txt==2):
        return "O"
    else:
        return " "    
# Function to validate the input value from the player
def inputValidation(player, tabl, history):
    rep=False
    while(rep==False):
        buffer=str(input(f"\nEnter move player 0{player}: "))
        for i in range(len(authorizedListe)):
            if(buffer==authorizedListe[i]): # compare with the authorizedListe of input move
                rep=True    
        if rep==True:
            for i in range(len(history)): # compare with the previous inputs move
                if(buffer==history[i]):
                    rep=False
        if rep==False:
            print(chr(27) + "[2J")  # Clear the terminal with escape sequences
            print(f"Bad input player 0{player} --- Please re-enter (ex: a1, b2,...)\n")
            showboard(tabl) # Show the board(table)   
    return buffer
# Function to apply the move (m) of a player in the table
def sendMove(tabl, m, player, history):
    match m :
        case 'a1':
            tabl[0,0]=player
        case 'a2':
            tabl[1,0]=player
        case 'a3':
            tabl[2,0]=player
        case 'b1':
            tabl[0,1]=player
        case 'b2':
            tabl[1,1]=player
        case 'b3':
            tabl[2,1]=player
        case 'c1':
            tabl[0,2]=player
        case 'c2':
            tabl[1,2]=player           
        case 'c3':
            tabl[2,2]=player
    history.append(m)
# Function to verify if is there a winner or not
def isThereWinner(tabl):
    if (tabl[0,0]+tabl[1,1]+tabl[2,2]==3 or tabl[0,2]+tabl[1,1]+tabl[2,0]==3 or
        tabl[0,0]+tabl[0,1]+tabl[0,2]==3 or tabl[1,0]+tabl[1,1]+tabl[1,2]==3 or tabl[2,0]+tabl[2,1]+tabl[2,2]==3 or
        tabl[0,0]+tabl[1,0]+tabl[2,0]==3 or tabl[0,1]+tabl[1,1]+tabl[2,1]==3 or tabl[0,2]+tabl[1,2]+tabl[2,2]==3):
        print("\nPlayer 01 Wins!!!\n")
        return True
    elif (tabl[0,0]+tabl[1,1]+tabl[2,2]==6 or tabl[0,2]+tabl[1,1]+tabl[2,0]==6 or
        tabl[0,0]+tabl[0,1]+tabl[0,2]==6 or tabl[1,0]+tabl[1,1]+tabl[1,2]==6 or tabl[2,0]+tabl[2,1]+tabl[2,2]==6 or
        tabl[0,0]+tabl[1,0]+tabl[2,0]==6 or tabl[0,1]+tabl[1,1]+tabl[2,1]==6 or tabl[0,2]+tabl[1,2]+tabl[2,2]==6):
        print("\nPlayer 02 Wins!!!\n")
        return True
    else:
        return False  

# Get move IA
def get_move_ia(history, authorizedListe):
    rep=False
    while(rep==False):
        row=random.randint(1,3)
        match row :
            case 1:
                row='a'
            case 2:
                row='b'
            case 3:
                row='c'
        col=random.randint(1,3)
        m=row+str(col)
        for i in range(len(authorizedListe)):
            if(m==authorizedListe[i]): # compare with the authorizedListe of input move
                rep=True    
        if rep==True:
            for i in range(len(history)): # compare with the previous inputs move
                if(m==history[i]):
                    rep=False
    return m
    
def allPossibleMove(authorizedListe, history):
    allowedMove=authorizedListe.copy()
    for i in history : 
        allowedMove.remove(i)
    return allowedMove

def betterMove(table, authorizedListe, history):
    allowedMove=allPossibleMove(authorizedListe, history).copy()
    winnerMove=allowedMove[0]
    isWinnerMove=False
    betterMove=winnerMove
    isBetterMove=False
    for m in allowedMove:
        #sendMove
        table1=table.copy()
        match m :
            case 'a1':
                table1[0,0]=2
            case 'a2':
                table1[1,0]=2
            case 'a3':
                table1[2,0]=2
            case 'b1':
                table1[0,1]=2
            case 'b2':
                table1[1,1]=2
            case 'b3':
                table1[2,1]=2
            case 'c1':
                table1[0,2]=2
            case 'c2':
                table1[1,2]=2           
            case 'c3':
                table1[2,2]=2
        #isThereWinner
        if (table1[0,0]+table1[1,1]+table1[2,2]==6 or table1[0,2]+table1[1,1]+table1[2,0]==6 or
            table1[0,0]+table1[0,1]+table1[0,2]==6 or table1[1,0]+table1[1,1]+table1[1,2]==6 or table1[2,0]+table1[2,1]+table1[2,2]==6 or
            table1[0,0]+table1[1,0]+table1[2,0]==6 or table1[0,1]+table1[1,1]+table1[2,1]==6 or table1[0,2]+table1[1,2]+table1[2,2]==6):
            #print("There is a winner move!")
            isWinnerMove=True
            winnerMove=m
            break
    if isWinnerMove==False:
        for m in allowedMove:
            #sendMove
            table1=table.copy()
            match m :
                case 'a1':
                    table1[0,0]=1
                case 'a2':
                    table1[1,0]=1
                case 'a3':
                    table1[2,0]=1
                case 'b1':
                    table1[0,1]=1
                case 'b2':
                    table1[1,1]=1
                case 'b3':
                    table1[2,1]=1
                case 'c1':
                    table1[0,2]=1
                case 'c2':
                    table1[1,2]=1           
                case 'c3':
                    table1[2,2]=1
            #isThereWinner
            if (table1[0,0]+table1[1,1]+table1[2,2]==3 or table1[0,2]+table1[1,1]+table1[2,0]==3 or
                table1[0,0]+table1[0,1]+table1[0,2]==3 or table1[1,0]+table1[1,1]+table1[1,2]==3 or table1[2,0]+table1[2,1]+table1[2,2]==3 or
                table1[0,0]+table1[1,0]+table1[2,0]==3 or table1[0,1]+table1[1,1]+table1[2,1]==3 or table1[0,2]+table1[1,2]+table1[2,2]==3):
                #print("There is a better move!")
                isBetterMove=True
                betterMove=m
                break
        return betterMove
    else:
        return winnerMove
    
# Set initial variables : table, history, authorizedListe, rnd
table=np.array(([8,8,8],[8,8,8],[8,8,8]))
history=[]
authorizedListe=['a1','a2','a3','b1','b2','b3','c1','c2','c3']
rnd=2
# The main loop
while(True):
    print(chr(27) + "[2J")  # Clear the terminal with escape sequences
    showboard(table) # Show the board(table)
    if len(history)>=9 : # Verify if players played all possible cases on the board
        print("\nDraw game\n")
        exit()
    #print(history) # To show move history
    if(isThereWinner(table)): # Verify Winner
        exit()
    if(rnd==1):
        play=inputValidation(rnd, table, history) # Ask player to play
        sendMove(table, play, rnd, history) # Send move to the board(table)
    elif(rnd==2):
        #play = get_move_ia(history, authorizedListe)
        play=betterMove(table,authorizedListe,history)
        sendMove(table, play, rnd, history)
    
    rnd=(1^(rnd-1))+1 # passer de joueur 1 à 2, puis de joueur 2 à 1 la boucle suivante, et ainsi de suite...
