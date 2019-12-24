from fonctions_plateau import*

letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
list_move = []
victory = False
nbr_x = 2
nbr_o = 2
turn = 1
to_flip = []
valid = False

size = int(input("What size do you want your board to be ? : "))
        
plateau_create(size)
plateau = plateau_create(size)
plateau_center(size, plateau)
valid_moves = []
to_flip = []


while(victory != True) :
    print(" ")
    afficher_plateau(plateau)
    valid_moves = get_valid_moves(plateau, turn)
    commands_infos_affichage(turn,nbr_x,nbr_o, valid_moves)
    end_turn = False
    while (end_turn != True) :
        choice = input("What do you want to do ? : ")
        if (choice == "P") :
            if (len(valid_moves) != 0) :
                row = input("Please enter the row : ")
                column = letter_to_number(size)
                row = int(row)
                column = int(column)
                valid = check_if_possible(plateau, column, row, turn)
                if (valid != False) :
                    if (turn % 2 == 0) :
                        plateau[row][column] = "\033[1;31m""o""\033[1;37m"
                    else :    
                        plateau[row][column] = "\033[1;34m""x""\033[1;37m"
                    to_flip = check_if_possible(plateau, column, row, turn)
                    plateau = flip_pawns(plateau, to_flip, turn)
                    end_turn = True
                else :
                    print("You can't place a pawn here.")
            else :
                print("You can't play this turn.")
        elif (choice == "S") :
            victory = True
            if (turn % 2 == 0) :
                victory_who = 1
                break
            else :
                victory_who = 2
                break
        elif (choice == "H") :
            hlp(valid_moves)
        elif (choice == "N") :
            if (len(valid_moves) == 0) :
                end_turn = True
            else :
                print("You can't pass your turn if you can play.")
                    
        else :
            valid = False
            print("You did something wrong, please make a choice again.")
    nbr_x = x_count(plateau, size)
    if (nbr_x == 0) :
        victory = True
        victory_who = 2
        break
    nbr_o = o_count(plateau, size)
    if (nbr_o == 0) :
        victory = True
        victory_who = 1
        break
    if (nbr_x + nbr_o == size * size) :
        if (nbr_o < nbr_x) :
            victory = True
            victory_who = 1
            break
        elif (nbr_o > nbr_x) :
            victory = True
            victory_who = 2
            break
        else :
            victory = True
            victory_who = 3
            
    turn = turn + 1
if (victory_who == 1) :
    print(" ")
    print("Player ""\033[1;34m""x""\033[1;37m"" wins !")
elif (victory_who == 2) :
    print(" ")
    print("Player ""\033[1;31m""o""\033[1;37m"" wins !")
else :
    print(" ")
    print("No winner, it's a draw.")
    


