# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    csvfile = open('stock.csv','r')   
    stock = list(csv.DictReader(csvfile))
    cant_arandelas = 0
    cant_tornillos = 0
    cant_tuercas = 0
    for i in range(len(stock)):
        articulos = stock[i]
        for k,v in articulos.items():
            if k == "arandelas":
                cant_arandelas += int(v)
            elif k == "tornillos":
                cant_tornillos += int(v)
            else:
                cant_tuercas += int(v)
    print("La cantidad de arandelas es de",cant_arandelas,"\n""La cantidad de tornillos es de",cant_tornillos,"\n"
    "y la cantidad de tuercas es de",cant_tuercas)
    csvfile.close()
    

def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    csvfile = open('propiedades.csv','r')     
    propiedades = list(csv.DictReader(csvfile))
    n_amb = 0
    dos_amb = 0
    tres_amb = 0
    err = 0
    for i in range(len(propiedades)):       # Cantidad de ítems: 1049
        depto = propiedades[i]
        for k,v in depto.items():
            try:
                ambientes = int(v)
                if ambientes == 2:
                    dos_amb += int(v)
                elif ambientes == 3:
                    tres_amb += int(v)
                elif ambientes == " ":
                    err += int(v)
                else:
                    n_amb += int(v)
            except:
                print("Hay deparatamentos que no especifican...")          
    print("Departamentos de dos ambientes:",dos_amb)
    print("Departamentos de tres ambientes:",tres_amb)
    print("Departamentos sin especificar:",err)
    print('Errores:',n_amb)
   
    csvfile.close()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
