def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    pass

def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    pass

def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    pass



# rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# board = [[[False for r in range(10)] for f in range()]]

pintar = []

for i in range(3):
    row = []
    for j in range(3):
        row.append('-')
    pintar.append(row)


for row in pintar:
    for item in row:
        print( item, end=" ")
    print()

for i in range(3):
    print('+' + '-'*(7) + '+' + '-'*(7) + '+' + '-'*(7) + '+')
    for j in range(3):
        print('|' + ' ' * (7) + '|' + ' ' * (7) + '|' + ' ' * (7) + '|')
        j+=1
        if j == 2:
            print('|' + " "*(3) + item + " " * (3) + '|' + " "*(3) + item + " " * (3) + '|' + " " *(3) + item + " " * (3) + '|')

print('+' + '-'*(7) + '+' + '-'*(7) + '+' + '-'*(7) + '+')
   
    

# for i in range(1):
#     row = ["+" for i in range(4)]
#     pintar.append(row)
#     for i in range(1):
#         row = ["-" for i in range(8)]
#         pintar.append(row)

# for i in range(5):
#     print('1' * (5 - i - 1) + "*" * (2*i+1))
    
# for i in range(10):
#     print(' + ' * ( i-1) + " - " * (2*i+1))