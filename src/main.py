from person import Autor
from book import *

def main() -> None:
   # nombre = str(input('Digite el nombre del autor: '))
   # cedula = int(input('Digite la cédula del autor: '))
    
   # autor = Autor(nombre, cedula)

   # print (autor)

   libro_1 = Libroimpreso(
       titulo = 'Cien años de soledad',
       isbn = '1233436576',
       genero = 'Novela',
       formato = 'Pasta Dura',
       valor = 85000.0,
       paginas = 496,
       num_ejemplares= 5

   )

   libro_2 = Librodigital(
        titulo = 'El aliento de los dioses',
       isbn = '3543456456',
       genero = 'Novela',
       formato = 'Pdf',
       valor = 60000.0,
       has_hipervinculo= True

   )
   libro_3 = Audiolibro(
        titulo = 'Harry Potter',
       isbn = '56732454565',
       genero = 'Novela',
       formato = 'mp4',
       valor = 50000.0,
       duracion = 330

   )

   print (libro_1)
   print (libro_2)
   print (libro_3)
if __name__ == '__main__':
    main()