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
          

    