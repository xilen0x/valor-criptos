from sqlalchemy import true


#set1 = {10, 20, 30, 40, 20, 80}
set1 =set()
set2 = {60, 70, 80, 90, 70}


def typesOfSets(opttion):

    if opttion == 1:
        set3 = set1 | set2
        print("Set unión: ", set3)
    elif opttion == 2:
        set3 = set1 & set2
        print("Set intersección: ", set3)

    elif opttion == 3:
        set3 = set1-set2
        print("Set diferencia: ", set3)

    elif opttion == 4:
        set3 = set1 ^ set2
        print("Set diferencia simétrica: ", set3)

    else:
        print("Bad Option")

status = True
while status:
    optionSet1 = int(input("Ingrese un valor para almacenar en el set1:"))
    set1.add(optionSet1)
    yesOrNot = input("Desea ingresar otro valor?: (y/n)").lower()
    if yesOrNot == "y" or status == "yes":
        continue
    elif yesOrNot == "n" or yesOrNot == "not":
        print(set1)
        status = False
    else:
        print("Opción incorrecta!")
        status = False

#print(set1)
print(set2)
print("""
        1.- Unión (Selecciona todos los elementos de ambos sets, dejando solo 1 elemento en el caso de repetirse alguno)
        2.- Intersección (Selección de solo los elementos comunes en ambos sets y eliminando repetidos)
        3.- Diferencia (Todos los elementos del primer set, eliminando aquellos elementos comunes con el set2 y eliminando repetidos)
        4.- Diferencia simétrica (Todos los elementos de ambos sets, eliminando aquellos elementos comunes y eliminando repetidos)
        """)

opttion = int(input("Ingrese una opción:"))
typesOfSets(opttion)
