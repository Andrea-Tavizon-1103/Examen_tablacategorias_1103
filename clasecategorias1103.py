print("examen con tabla categorias")
print("Andrea Tavizon Mat: 22308051281103")
#zona de la clase
class categorias1103:
#zona de atributos dentro de la clase
    id_categoria= 0
    nombre= ""
    descripcion= ""
    fecha_creacion= ""
    estado= ""
    orden = 0
    marca = ""
#zona de funciones dentro de la clase
    def mostrarcategorias1103(self,c):
        print(f"ID categoria: {c}")
        print(f"Nombre: {c}")
        print(f"Descripcion: {c}")
        print(f"Fecha de creacion: {c}")
        print(f"Estado: {c}")
        print(f"Orden: {c}")
        print(f"Marca: {c}")
class mostrar:
    def listar_categorias(self):
        productos = ["id_categoria", "Nombre", "Descripcion", "Fecha de creacion", "Estado"]
        for x in productos :
            print(x)
    
    def tupla_categorias(self):
        tuplaCAtego = ("id_categoria", "Nombre", "Descripcion", "Fecha de creacion", "Estado")
        print(tuplaCAtego)
        for tuplaCAtego in tuplaCAtego:
            print(tuplaCAtego)

    def diccionario_categorias(self):
        dicc = {
            "ID:": 2345,
            "Nombre:": "Cargador",
            "Marca:": "Motorola",
            "Estado:": "Chihuahua",
            "Descripcion:": "Entrada tipo C"
        }    
        for x, y in dicc.items():
            print(x,y)
    def alta_dicc(self):
        print("Se dio de alta el pedido de el cargador")
    def baja_dicc(self):
        print("Se dio de baja el producto cargador")                     
    
#zona de creacion de objetos        
producto=categorias1103()
#zona de usando objetos
print("resultado para el producto: ")
producto.id_categoria= 123
producto.nombre= "Audifonos"
producto.descripcion= "Audifonos inalambricos"
producto.fecha_creacion= "24/09/23"
producto.estado= "Chihuahua"
producto.orden = 50
producto.marca = "Motorola"
print(f"ID categoria: {producto.id_categoria}")
print(f"Nombre: {producto.nombre}")
print(f"Descripcion: {producto.descripcion}")
print(f"Fecha de creacion: {producto.fecha_creacion}")
print(f"Estado: {producto.estado}")
print(f"Orden: {producto.orden}")
print(f"Marca: {producto.marca}")
datos=mostrar()
print("Se muestran las listas")
datos.listar_categorias()
print("Mostrar tuplas")
datos.tupla_categorias()
print("Se muestran los diccionarios")
datos.diccionario_categorias()





