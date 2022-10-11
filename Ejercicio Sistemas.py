cod_articulo = {}
nombre = {}
descripcion = {}
precio = {}


def Altas():print("")

print("Introduzca los datos del articulo")
cod_articulo = input("Ponga el codigo del articulo: ")
nombre = input("Introduzca el nombre del articulo: ")
descripcion = input("Introduzca la descripcion del articulo: ")
precio = input("Introduzca el precio del articulo: ")

Articulo = [cod_articulo,nombre,descripcion, precio]

print(Articulo)

def Bajas (): 
 print("")

print("----------------------------------------------------------")

for n in Articulo: 
    print(n)

borrar = input("Borre la posición que quiera eliminar (las possiciones van desde el 0 al 3)")

Articulo.pop(int(borrar))
Articulo.insert(int(borrar),"   ")

print("Se ha eliminado de manera correcta")
print(Articulo)


def Cambios():
    print("")

print("-----------------------------------------------------------")

for n in Articulo:
    print(n)

borrar = input("Seleccione la casilla")
Modificar = input("Modifique el articulo que desee")

Articulo.pop(int(borrar))
Articulo.insert(int(borrar),Modificar)

print("El articulo se ha añadido correctamente ")
print(Articulo)

def busqueda():
    print("")

print("------------------------------------------")

for n in Articulo:
    print(n)

buscar = input("Introduce el numero en forma de busca del articulo que quieres buscar (los numeros van desde el 0 al 3)")
print(Articulo[int(buscar)])

def Lista():
    print("")

print("------------------------------------------------")
Listado = input("Asi queda la lista actualmente (Pulse enter)")
print(Articulo)