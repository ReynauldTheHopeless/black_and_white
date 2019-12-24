def plateau_create(size) :       #créé le plateau vide
    letters = ["\033[1;33m"" A""\033[1;37m", "\033[1;33m""B""\033[1;37m", "\033[1;33m""C""\033[1;37m", "\033[1;33m""D""\033[1;37m", "\033[1;33m""E""\033[1;37m", "\033[1;33m""F""\033[1;37m", "\033[1;33m""G""\033[1;37m", "\033[1;33m""H""\033[1;37m", "\033[1;33m""I""\033[1;37m", "\033[1;33m""J""\033[1;37m", "\033[1;33m""K""\033[1;37m", "\033[1;33m""L""\033[1;37m", "\033[1;33m""M""\033[1;37m", "\033[1;33m""N""\033[1;37m", "\033[1;33m""O""\033[1;37m", "\033[1;33m""P""\033[1;37m", "\033[1;33m""Q""\033[1;37m", "\033[1;33m""R""\033[1;37m", "\033[1;33m""S""\033[1;37m", "\033[1;33m""T""\033[1;37m", "\033[1;33m""U""\033[1;37m", "\033[1;33m""V""\033[1;37m", "\033[1;33m""W""\033[1;37m", "\033[1;33m""row""\033[1;37m", "\033[1;33m""column""\033[1;37m", "\033[1;33m""Z""\033[1;37m"]
    numbers = ["\033[1;33m""1 ""\033[1;37m", "\033[1;33m""2 ""\033[1;37m", "\033[1;33m""3 ""\033[1;37m", "\033[1;33m""4 ""\033[1;37m", "\033[1;33m""5 ""\033[1;37m", "\033[1;33m""6 ""\033[1;37m", "\033[1;33m""7 ""\033[1;37m", "\033[1;33m""8 ""\033[1;37m", "\033[1;33m""9 ""\033[1;37m", "\033[1;33m""10""\033[1;37m","\033[1;33m""11""\033[1;37m", "\033[1;33m""12""\033[1;37m", "\033[1;33m""13""\033[1;37m", "\033[1;33m""14""\033[1;37m", "\033[1;33m""15""\033[1;37m", "\033[1;33m""16""\033[1;37m", "\033[1;33m""17""\033[1;37m", "\033[1;33m""18""\033[1;37m", "\033[1;33m""19""\033[1;37m", "\033[1;33m""20""\033[1;37m", "\033[1;33m""21""\033[1;37m", "\033[1;33m""22""\033[1;37m", "\033[1;33m""23""\033[1;37m", "\033[1;33m""24""\033[1;37m", "\033[1;33m""25""\033[1;37m", "\033[1;33m""26""\033[1;37m",]
    plat = []
    plat = [[" "] * (size + 1) for i in range(size + 1)]
    for i in range(size) :
        plat[i + 1][0] = numbers[i]
    for j in range(size) :
        plat[0][j + 1] = letters[j]
    for i in range(size) :
        for j in range(size) :
            plat[i + 1][j + 1] = "*"
    return plate loop
        user_choice = input("Please enter the column : ")
        if (user_choice in dict_alphabet):
            ind = dict_alphabet[user_choice]  

def plateau_center(size, plateau) :       #ajoute au plateau les cases du milieu (c_prise n'est pas encore bien configuré)
    c_prise = [[" "] * (2) for i in range(size * size)]
    plateau[int(size / 2)][int(size / 2)]="\033[1;31m""o""\033[1;37m"
    plateau[int(size / 2 + 1)][int(size / 2)]="\033[1;34m""x""\033[1;37m"
    plateau[int(size / 2)][int(size / 2 + 1)]="\033[1;34m""x""\033[1;37m"
    plateau[int(size / 2 + 1)][int(size / 2 + 1)]="\033[1;31m""o""\033[1;37m"
    
    return c_prise

def letter_to_number(size)  :
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    list_alphabet = list(alphabet)
    max_size = size
    dict_alphabet = dict()
    num = 1
    for letter in list_alphabet:
        dict_alphabet[letter] = num
        if (num == max_size):
            break
        num += 1
    while True : # while loop
        user_choice = input("Please enter the column : ")
        if (user_choice in dict_alphabet):
            ind = dict_alphabet[user_choice]  
        else:
            print ("Wrong letter, try again.")
        return(ind)

def number_to_letter(number) :
    letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    number = letters[number - 1]
    return number
    
    

def afficher_plateau(plateau) :
    for l in plateau :
        print(" ".join([str(a) for a in l]))
        
def x_count(plateau, size) :
    nbr_x = 0
    for i in range(size + 1) :
        for j in range(size + 1) :          
            if (plateau[i][j] == "\033[1;34m""x""\033[1;37m") :
                nbr_x = nbr_x + 1
            else :
                size = size
    return nbr_x

def o_count(plateau, size) :
    nbr_o = 0
    for i in range(size + 1) :
        for j in range(size + 1) :          
            if (plateau[i][j] == "\033[1;31m""o""\033[1;37m") :
                nbr_o = nbr_o + 1
            else :
                size = size
    return nbr_o
        
def commands_infos_affichage(turn,nbr_x,nbr_o, valid_moves) :
    print(" ")
    print("Turn n° :", "\033[1;35m",turn,"\033[1;37m")
    print(" ")
    if (turn % 2 == 0) :
        print("It is ""\033[1;31m""o""\033[1;37m"" turn's.")
    else :
        print("It is ""\033[1;34m""x""\033[1;37m"" turn's.")
    print(" ")
    print("\033[1;34m""x""\033[1;37m"" on the board : ", nbr_x)
    print("\033[1;31m""o""\033[1;37m"" on the board : ", nbr_o)
    print(" ")
    if (len(valid_moves) != 0) :
        print("Enter ""\033[1;35m""P""\033[1;37m"" to place a pawn.")
        print("Enter ""\033[1;32m""H""\033[1;37m"" to see the possible moves.")
    else :
        print ("You can't play this turn.")
        print("Enter ""\033[1;33m""N""\033[1;37m"" to go to the next turn.")
    print("Enter ""\033[1;36m""S""\033[1;37m"" to surrender.")
    print(" ")
    
def check_if_possible(plateau, column, row, turn):
    row_list = [0,1,1,1,0,-1,-1,-1]
    col_list = [1,1,0,-1,-1,-1,0,1]
    if (turn % 2 == 0) :
        enn = "\033[1;34m""x""\033[1;37m"
        nenn = "\033[1;31m""o""\033[1;37m"
    else :
        enn = "\033[1;31m""o""\033[1;37m"
        nenn = "\033[1;34m""x""\033[1;37m"
    to_flip = []
    for i in range(0,7) :
        row_direction = row_list[i]
        col_direction = col_list[i]
        x = int(row)
        y = int(column)
        x = x + row_direction
        y = y + col_direction
        if (plateau[x][y] == enn) :
             x = x + row_direction
             y = y + col_direction
             while (plateau[x][y] == enn) :
                x = x + row_direction
                y = y + col_direction
             if (plateau[x][y] == nenn) :
                 x = x - row_direction
                 y = y - col_direction
                 to_flip.append([x,y])
                 while (plateau[x][y] != nenn) :
                     x = x - row_direction
                     y = y - col_direction
                     if (x == row and y == column) :
                         break
                     to_flip.append([x,y])
        else :
            continue
    if (len(to_flip) == 0) :
        return False
    return to_flip

def get_valid_moves(plateau, turn) :
    valid_moves = []
    for x in range(8):
        for y in range(8):
            if check_if_possible(plateau, y, x, turn) != False:
                valid_moves.append([x, y])
    return valid_moves

def flip_pawns(plateau, to_flip, turn) :
    row_to_flip = []
    col_to_flip = []
    if (turn % 2 == 0) :
        enn = "\033[1;31m""o""\033[1;37m"
    else :
        enn = "\033[1;34m""x""\033[1;37m"
    for i in range(0,len(to_flip)) :
        row_to_flip.append(to_flip[i][0])
        col_to_flip.append(to_flip[i][1])
    for i in range(0,len(to_flip)) :
        row = row_to_flip[i]
        col = col_to_flip[i]
        plateau[row][col] = enn
    return (plateau)

def hlp(valid_moves) :
    for i in range(0, len(valid_moves)) :
        print(valid_moves[i][0], end = '')
        print("\033[1;32m",number_to_letter(valid_moves[i][1]),"\033[1;37m","  ")
        
                           
        
    
        
                    

            
            
    
    
    