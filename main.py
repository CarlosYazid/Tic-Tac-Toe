from random import randint as rand

def run():
    #Tablero inicial: Son solo numeros
    board = [ [i for i in range(((j - 1) * 3) + 1,(j * 3) + 1)] for j in range(1,4)]

    #Jugador Base
    player = "Machine"

    #Primer Movimiento por defecto
    board[1][1] = "X"
    
    #Display del Tablero
    board_ = f"""
            +--------+--------+--------+
            |        |        |        |
            |    {board[0][0]}   |   {board[0][1]}    |    {board[0][2]}   |
            |        |        |        |
            +--------+--------+--------+
            |        |        |        |
            |    {board[1][0]}   |   {board[1][1]}    |    {board[1][2]}   |
            |        |        |        |
            +--------+--------+--------+
            |        |        |        |
            |    {board[2][0]}   |   {board[2][1]}    |    {board[2][2]}   |
            |        |        |        |
            +--------+--------+--------+"""
    
    
    
    #Imprime el tablero por primera vez
    print(board_)

    def display_board(board): #Funcion que imprime el tablero cuando sea necesario

        board_ = f"""
            +--------+--------+--------+
            |        |        |        |
            |    {board[0][0]}   |   {board[0][1]}    |    {board[0][2]}   |
            |        |        |        |
            +--------+--------+--------+
            |        |        |        |
            |    {board[1][0]}   |   {board[1][1]}    |    {board[1][2]}   |
            |        |        |        |
            +--------+--------+--------+
            |        |        |        |
            |    {board[2][0]}   |   {board[2][1]}    |    {board[2][2]}   |
            |        |        |        |
            +--------+--------+--------+"""
        
        print(board_)
    
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
            
            x = board[int(move // 3.1)][int(move // 3.1)]
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
            board[int(move // 3.1)][int(move // 3.1)] = "O"
            display_board(board)
            player = "Machine"
            move = rand(1,9)
            verify_move(board, move, player)

        elif player == "Machine":
            board[int(move // 3.1)][int(move // 3.1)] = "X"
            player = "User"
            display_board(board)

    def win(board): #Verifica si hay un ganador

        win = "none"
        board_lineal = []
        for i in board:
            for j in i:
                board_lineal.append(j)

        for i in board:
            if all(i) and i[0] == "O":
                win = "User"
            elif all(i) and i[0] == "X":
                win = "Machine"
        for i in list(zip(*board)): #Se verifica si alguna fila o columna este llena de algun movimiento en especifico
            if all(i) and i[0] == "O":
                win = "User"
            elif all(i) and i[0] == "X":
                win = "Machine"
        
        #Tambien se hace la verificación por diagonal1es
        diag1 = [board[0][0],board[1][1],board[2][2]]
        diag2 = [board[0][2],board[1][1],board[2][0]]

        if all(diag1) and diag1[0] == "O":
            win = "User"
        elif all(diag1) and diag1[0] == "X":
            win = "Machine"
        elif all(diag2) and diag2[0] == "O":
            win = "User"
        elif all(diag2) and diag2[0] == "X":
            win = "Machine"

        tie = []
        for i in board_lineal:
            if isinstance(i,str):
                tie.append("str")
        if all(tie):
            win = "tie"


        print(f"{win}")

        return win

    while True:
        enter_move(board)
        if win(board) == "none":
            enter_move(board)
        elif win(board) == "tie":
            print("tie")
            break
        else:
            print(f"{win(board)} has won the game!")
            break


if __name__ == "__main__":
    run()

