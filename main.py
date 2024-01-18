from random import randint as rand

def run():
    #Tablero inicial: Son solo numeros
    def matrix_generator_nXn(n):
        return [[j for j in range((i - 1) * n + 1, (i) * n + 1)] for i in range(1, n + 1)]

    board = matrix_generator_nXn(3)

    def display_board(matrix): #Funcion que imprime el tablero cuando sea necesario
        board_display = ""
        cant_rows = len(matrix)
        x1 = "+---------" * cant_rows + "+"
        x2 = "|         " * cant_rows + "|"
        for row in matrix:
            x3 = "".join(["|    " + str(element) + "    " for element in row]) + "|"
            if matrix.index(row) == 0:
                board_display += (x1+"\n"+x2+"\n"+x3+"\n"+x2+"\n"+x1+"\n")
            elif matrix.index(row) == (cant_rows - 1):
                board_display += (x2+"\n"+x3+"\n"+x2+"\n"+x1)
            else:
                board_display += (x2+"\n"+x3+"\n"+x2+"\n"+x1+"\n")
        print(board_display)
    
    display_board(board) #Imprime el tablero por primera vez
    
    def enter_move(board): #Funcion que recibe el movimiento del jugador
        try:
            move = int(input("Enter move: "))
        except:
            move = False
        
        #Evitamos caracteres invalidos

        if move == False:
            print("Invalid move: You entered invalid characters \n")
            display_board(board)
            enter_move(board)
        elif (move < 1) or (move > 9):
            print("Invalid move: You entered numbers that are not within the range \n") #Evitamos movimientos Fuera de rango
            display_board(board)
            enter_move(board)
        else:
            player = "User"
            verify_move(board, move, player)

            #Despues de hacer una verificación basica del movimiento ejecutamos la segunda funcion
        
    def verify_move(board, move, player): #Esta funcion verifica que el movimiento a realizar sea posible dependiendo si la casilla esta vacia o no
            
            x = board[int(move // 3.1)][int((move - 1)  % 3)]
            y = (x == "X" or x == "O")


            if win(board) == "none": #Hacemos esta verificacion para que en caso de que todas los casillas esten ocupadas no se entre en un bucle infinito por movimientos de la maquina
                if y and player == "User":
                    print("Invalid movement: movement is not possible because the space is occupied \n")
                    display_board(board)
                    enter_move(board)
                elif y and player == "Machine": #Nos aseguramos que si la maquina se equivoca haga otro movimiento hasta que sea valido
                    move = rand(1,9)
                    verify_move(board, move, player)
                else:
                    moving(board, move, player)
            elif win(board) == "tie":
                print("Tie")
                exit
            else:
                print(f"{win(board)} has won the game!")
                exit


    def moving(board,move, player):#Esta funcion coloca el movimiento en el tablero
        if player == "User":
            board[int(move // 3.1)][int((move - 1) % 3)] = "O"
            display_board(board)
            player = "Machine"
            move = rand(1,9)
            verify_move(board, move, player)

        elif player == "Machine":
            board[int(move // 3.1)][int((move - 1) % 3)] = "X"
            player = "User"
            display_board(board)

    def win(board): #Verifica si hay un ganador

        win = "none"
        board_lineal = []
        for i in board:
            for j in i:
                board_lineal.append(j)

        def some(list):
            x = list[0]
            for i in list:
                if x != i:
                    return False
            return True

        for i in board:
            if some(i) and i[0] == "O":
                win = "User"
            elif some(i) and i[0] == "X":
                win = "Machine"
        for i in list(zip(*board)): #Se verifica si alguna fila o columna este llena de algun movimiento en especifico
            if some(i) and i[0] == "O":
                win = "User"
            elif some(i) and i[0] == "X":
                win = "Machine"
        
        #Tambien se hace la verificación por diagonal1es
        diag1 = [board[0][0],board[1][1],board[2][2]]
        diag2 = [board[0][2],board[1][1],board[2][0]]

        if some(diag1) and diag1[0] == "O":
            win = "User"
        elif some(diag1) and diag1[0] == "X":
            win = "Machine"
        elif some(diag2) and diag2[0] == "O":
            win = "User"
        elif some(diag2) and diag2[0] == "X":
            win = "Machine"

        tie = []
        for i in board_lineal:
            if isinstance(i,str):
                tie.append(True)
            else:
                tie.append(False)

        if all(tie):
            win = "tie"

        return win

    while True:
        enter_move(board)
        if win(board) == "none":
            enter_move(board)
        elif win(board) == "tie":
            break
        else:
            break


if __name__ == "__main__":
    run()

