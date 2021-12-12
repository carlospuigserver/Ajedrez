def tablero(nombre_fichero,n):
    'Función que muestra por pantalla el tablero n de una partida de ajedrez'

f=open(nombre_fichero,'r')
tableros=f.read().split('\n')

for i in tableros[n*9,n*9+8]:
    print(i)

return

   

    