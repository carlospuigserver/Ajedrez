# Ajedrez

Dirección GitHub para este repositorio: https://github.com/carlospuigserver/Ajedrez.git



Para realizar este programa, es necesario controlar muy bien las listas, y sobre todo los bucles tanto for o while. Sinceramente no he tenido mucha idea de realizar el programa, y me he guiado en casi su plenitud por la página web a la que tenemos acceso a través del link que existe en la descripción del ejercicio 'Ajedrez'  en el campus virtual.





El diagrama de flujo relacionado con el programa es el siguiente:





<img width="955" alt="Ajedrez" src="https://user-images.githubusercontent.com/91721643/145732359-69a48404-7d1f-4186-82f2-1d53c20249a3.png">



Aquí dejo el link de figma por si la imagen no se ve correctamente: https://www.figma.com/file/NjVB7L57g8y8Aff5p3FdoO/Untitled?node-id=0%3A1







El código del programa es :
```
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


def tablero(nombre_fichero,n):
    'Función que muestra por pantalla el tablero n de una partida de ajedrez'

f=open(nombre_fichero,'r')
tableros=f.read().split('\n')

for i in tableros[n*9,n*9+8]:
    print(i)
return

