#Ahora crearemos una función donde se guarde los tableros de una partida de ajedrez en un fichero
def partida_ajedrez(nombre_fichero):
    'Función guardar tableros en fichero con parámetro para crear una cadeno con el nombre del fichero'

#El tablero se representa como una cadena,a partir de filas, usando el cambio de línea, y las colunas 
# a partir de tabuladores
tablero_I='♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖'

# Añadiremos las filas a partir de una lista vacía
tablero=[]

#Bucle para recorrer las filas del tablero
for i in tablero_I.split('\n'):
    tablero.append(i.split('\t'))
    fichero=open(nombre_fichero,'w') # Abrimos el fichero en modo escritura

for i in tablero:
    # Escribimos cada fila en una línea concatenando con cada caracter
    f.write('\t').join(i)+('\n')
    f.close()

# Empieza la partida con un contador de movimientos a 0
movimientos=0
while True:
    continuar=input('Deseas hacer otro movimiento?(si \ no):')
    if continuar != ('si'):
        break
    else:
        fila_origen=int(input('Introduce la fila de la pieza a mover'))
        columna_origen=int(input('Introduce la columna de la pieza a mover'))
        fila_destino=int(input('Introduce la fila de destino'))
        columna_destino=int(input('Introduce la columna de destino'))
        # Hacemos el movimiento en el tablero
        tablero[fila_destino-1][columna_destino-1]=tablero[fila_origen-1][columna_origen-1]=''
        movimientos+=1
        f=open(nombre_fichero,'a')
        #Añadimos una cadena con el nombre de movimientos
        f.write('Movimiento'+str(movimientos+ '\n'))
    
    for i in tablero:
     f.write('\t'.join(i)+'\n')
    f.close

return    

partida_ajedrez('partida1.txt')

def tablero(nombre_fichero,n):
    'Función que muestra por pantalla el tablero n de una partida de ajedrez'

f=open(nombre_fichero,'r')
tableros=f.read().split('\n')

for i in tableros[n*9,n*9+8]:
    print(i)
return
tablero('partida1.txt', 2)    

    