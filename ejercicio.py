juegos = {
'A123': ['FIFA 24', 'PS5', 'Deportes', 10],
'B456': ['Mario Kart 8', 'Switch', 'Carreras', 3],
'C789': ['The Last of Us II', 'PS5', 'Acción', 18],
'D321': ['Zelda BOTW', 'Switch', 'Aventura', 12],
'E654': ['Minecraft', 'PC', 'Creativo', 6]
}
ventas = {
'A123': [49990, 15],
'B456': [39990, 10],
'C789': [59990, 5],
'D321': [54990, 0],
'E654': [19990, 25]
}

def buscarporconsola(nombre):
    cantidad=0
    for i,j in juegos.items():
        if((j[1].lower() == nombre) and (i in ventas)):
            cantidad=cantidad+(ventas[i][1])
    print("la cantidad dispponible de ", nombre," es de:",cantidad)


def buscarjuegosporedad(min,max):
    juegosporrangoedad=[]
    for j,i in juegos.items():
        if(i[3]<=max and i[3]>=min) and (ventas[j][1]>0):
            juegosporrangoedad.append(i[0])
    if len(juegosporrangoedad)>0:
        print("el listado de juegos en este rango es ",juegosporrangoedad)
    else:
        print("no hay juegos en este rango de edades")


def actualizarprecio(cod,precio):
    if cod in ventas:
        ventas[cod][0]=precio
        return True
    else:
        return False

while (True):
    print("__________menu_________")
    print("1-Buscar por consola \n2-Juegos por rango de edad \n3-actualizar el precio del juego \n4-salir")
    try:
        op=int(input("ingrese su opcion de 1 a 4: "))
        if op==1:
            consola=input("ingrese el nombre de la consola: ")
            buscarporconsola(consola)
        elif(op==2):
            try:
                minedad=int(input("ingrese la edad minima: "))
                maxedad=int(input("ingrese la edad maxima: "))
                buscarjuegosporedad(minedad,maxedad)
            except ValueError as otro:
                print("ingrese la edad en numeros")
        elif(op==3):
            try:
                codigo=input("ingrese el codigo del juego: ")
                precio=int(input("ingrese el nuevo precio: "))
                if (actualizarprecio(codigo,precio)):
                    print("precio actualizado")
                else:
                    print("precio no actualizado")
            except ValueError as op3:
                print("ingrese numeros enteros")
        elif(op==4):
            print("saliendo.....")
            break
        else:
            print("opcion no valida ....")
    except ValueError:
        print("error...por favor ingrese un numero")

#para un segundo commit