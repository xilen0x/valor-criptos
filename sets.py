import os

set1 =set()
set2 = set()


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


def statusSets(sett):
    
    status = True

    while status:
        optionSet = int(input("Ingrese un valor para almacenar en el set{}:".format(sett)))
        
        if sett == 1:
            set1.add(optionSet)
            print(set1)
            yesOrNot = input("Desea ingresar otro valor?: (y/n)").lower()
            if yesOrNot == "y" or yesOrNot == "yes":
                continue
            elif yesOrNot == "n" or yesOrNot == "not":
                print(set1)
                status = False
            else:
                print("Opción incorrecta!")
                status = False
        elif sett ==2:
            set2.add(optionSet)
            print(set2)
            yesOrNot = input("Desea ingresar otro valor?: (y/n)").lower()
            if yesOrNot == "y" or yesOrNot == "yes":
                continue
            elif yesOrNot == "n" or yesOrNot == "not":
                print(set2)
                status = False
            else:
                print("Opción incorrecta!")
                status = False


def setChoice():
    os.system("clear")
    print("""
    1.- {}
    2.- {} """.format(set1, set2))
    opcion1 = int(input("Escoja un set de datos vacío: "))
    if opcion1 == 1:
        statusSets(opcion1) 
        os.system("clear")
    elif opcion1 == 2:
        statusSets(opcion1) 
        os.system("clear")
    else:
        print("No existe ese set de datos!")
    print(set1, set2)

#print(set1)
#print(set2)
setChoice()
setChoice()
print("""
SELECCIONE UNA OPCION:

        1.- Unión (Selecciona todos los elementos de ambos sets, dejando solo 1 elemento en el caso de repetirse alguno)
        2.- Intersección (Selección de solo los elementos comunes en ambos sets y eliminando repetidos)
        3.- Diferencia (Todos los elementos del primer set, eliminando aquellos elementos comunes con el set2 y eliminando repetidos)
        4.- Diferencia simétrica (Todos los elementos de ambos sets, eliminando aquellos elementos comunes y eliminando repetidos)
        """)

opttion = int(input("Opción: "))
typesOfSets(opttion)
