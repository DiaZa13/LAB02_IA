import os
from utilsia import readGraph, readSudoku, writeSudoku
from dijikstra import shortest_path

while True:
    os.system('cls')
    print("************ LABORATORIO 2 -INTELIGENCIA ARTIFICIAL- **************")
    print()

    choice = input("""
                          1 → Encontrar el camino más corto
                          2 → Resolver sudoku
                          3 → Salir
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
        read_file = input('Ingrese el nombre del archivo que define el Sudoku: ')
        size, restrictions_count, board = readSudoku(read_file)
        write_file = input('Ingrese el nombre del archivo que guardara las soluciones: ')
        writeSudoku(write_file, board, size)
        print(f'La soluciones se han guardado en {write_file}')
        input("\nPulsa una tecla para continuar")
    elif choice == "3":
        break
    else:
        print()
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")