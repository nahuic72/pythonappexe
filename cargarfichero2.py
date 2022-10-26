# argparse es la librería que nos permite capturar argumentos
import argparse
from pandas import read_csv

# creamos el parser
parser = argparse.ArgumentParser(
    prog = 'cargarfichero2',
    usage = '%(prog)s fichero_a_cargar.csv lineas_a_imprimir',
    description = 'Carga un fichero csv a partir del argumento e imprime las lineas que queramos',
    )

# añadimos los argumentos que queremos pedir.
parser.add_argument('fichero', 
                    action = "store",
                    help = 'nombre del fichero a cargar',
                    )

parser.add_argument('lineas', 
                    action = "store",
                    help = 'lineas a imprimir',
                    )
                    
# ejecutamos el método parse_args()
# en file.fichero se encuentra el texto que hemos introducido
argumentos = parser.parse_args()  

# tu programa, sea como sea

# carga los datos
print('Cargando fichero: ...',argumentos.fichero)
# dataset = np.loadtxt(file.fichero, delimiter=",")
dataset = read_csv(argumentos.fichero, delimiter=",")
      
# dividido en variables de entrada (X) y salida (Y)

print(dataset.head(int(argumentos.lineas)))

