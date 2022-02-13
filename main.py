import os
from utilsia import readGraph
from dijikstra import shortest_path
while True:
    # Mostramos el menu
    os.system('cls')
    print("************ LABORATORIO 2 -INTELIGENCIA ARTIFICIAL- **************")
    print()

    choice = input("""
                          1 → Encontrar el camino más corto
                          2 → Resolver sudoku de 4*4
                          3 → Resolver sudoku de 6*6
                          4 → Resolver sudoku de 9*9
                          5 → Salir
                          Ingrese una opción: """)

    if choice == "1":
        print()
        file = input('Ingrese el nombre del archivo que define el grafo: ')
        node_count, edges_count, vertices = readGraph(file)
        origin = int(input('Ingrese el nodo origen: '))
        destiny = int(input('Ingrese el nodo destino: '))
        shortest_path = shortest_path(node_count, vertices, origin, destiny)
        print(shortest_path)
        input("\nPulsa una tecla para continuar")
    elif choice == "2":
        print()
        os.system('cls')
        while True:
            print("************ PROCESO DE AUTENTICACIÓN DE ARCHIVOS **************")
            inner_choice = input("""
                                        1 → Generar los códigos hash de los archivos de texto 
                                        2 → Compararción entre los códigos hash (debe de generar los códigos hash antes)
                                        3 → Regresar al menú principal
                                        Ingrese una opción: """)
            if inner_choice == "1":
                print()
                password = input('Ingrese una contraseña: ')
                hash[0] = generateHashCodes(file=FILES[0], key=password)
                hash[1] = generateHashCodes(file=FILES[1], key=password)
                print(f"Hash1 {hash[0].hexdigest()}\nHash2 {hash[1].hexdigest()}\n{compareHash(hash[0], hash[1])}")
                input("\nPulsa una tecla para continuar")
            elif inner_choice == "2":
                if not hash[0]:
                    print("Aún no se han generado los códigos hash")
                else:
                    print()
                    print('Ingrese que código Hash desea comparar')
                    print('1. hash del texto1')
                    print('2. hash del texto2')
                    try:
                        option1 = int(input('Ingrese el primer hash a comparar: '))
                        option2 = int(input('Ingrese el segundo hash a generar nuevamente y a comparar: '))
                        password = input('Ingrese una contraseña: ')
                        hash2 = generateHashCodes(file=FILES[option2 - 1], key=password)
                        print(
                            f"Hash1 {hash[option1 - 1].hexdigest()}\nHash2 {hash2.hexdigest()}\n{compareHash(hash[option1 - 1].hexdigest(), hash2.hexdigest())}")
                    except:
                        print("Datos invalidalos")
                    input("\nPulsa una tecla para continuar")
            elif inner_choice == "3":
                break

        print()
    elif choice == "3":
        print()
        while True:
            os.system('cls')
            print("************ PROCESO DE AUTENTICACIÓN DE USUARIOS **************")
            inner_choice = input("""
                                      1 → Registrarse
                                      2 → Iniciar sesión
                                      3 → Regresar a menú principal

                                      Ingrese una opción: """)
            if inner_choice == "1":
                print()
                user = input('Nombre de usuario: ')
                password = input('Contraseña: ')
                print(register(user, password))
                input("\nPulsa una tecla para continuar")
            elif inner_choice == "2":
                print()
                user = input('Nombre de usuario: ')
                password = input('Contraseña: ')
                print(login(user, password))
                input("\nPulsa una tecla para continuar")
                print()
            elif choice == "3":
                break
    elif choice == "4":
        break
    else:
        print()
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")