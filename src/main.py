from person import Autor

def main() -> None:
    nombre = str(input('Digite el nombre del autor: '))
    cedula = int(input('Digite la cédula del autor: '))
    
    autor = Autor(nombre, cedula)

    print (autor)
if __name__ == '__main__':
    main()