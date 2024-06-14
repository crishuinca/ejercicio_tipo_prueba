import os, time, msvcrt
trabajadores = []
cargos = ("CEO", "DESARROLLADOR", "ANALISTA")

def opcion_1():
    os.system("cls")
    print( "REGISTRAR TRABAJADOR")
    time.sleep(1)
    os.system("cls")
    nombre_apellido = input("Ingrese nombre y apellido: ")
    cargo = int(input("Ingrese cargo(1:CEO, 2:DESARROLLADOR, 3: ANALISTA): "))
    sueldo_bruto = int(input("Ingrese sueldo bruto: "))
    desc_salud = int(7/100 * sueldo_bruto)
    desc_afp = int(12/100 * sueldo_bruto)
    sueldo_liquido = round(sueldo_bruto-desc_afp-desc_salud)
    trabajador = [nombre_apellido , cargos[cargo - 1] , sueldo_bruto ,desc_afp , desc_salud , sueldo_liquido] #Se mete en la tupla "cargos" y resta 1
    trabajadores.append(trabajador)
    print("TRABAJADOR REGISTRADO CON EXITO!") 

def opcion_2():
    if len(trabajadores) == 0:
            print("No existen trabajadores, elija la opción 1")
    else:
        print("\tLista de trabajadores")
        print("Trabajador \tCargo \tSueldo Bruto \tDes. Salud \t Des. AFP \tLiquido a pagar")
        for t in trabajadores:  # t seria cada trabajador de la lista, t es una lista dentro de otra lista
            
            for x in range(6):
                print(f"{t[0]}\t{t[1]}\t\t{t[2]}\t\t{t[3]}\t\t{t[4]}\t\t{t[5]}")

def opcion_3():
    if len(trabajadores) == 0:
        print("No existen trabajadores, elija la opción 1")
    else:
        opc2 = int(input("¿Que cargo desea imprimir (1.CEO 2.DESARROLLADOR 3.ANALISTA 4.TODOS): "))
        if opc2== 4:
            with open("todos_trabajadores.txt", "w", newline="\n" )as archivo:
                for t in trabajadores:
                    texto = f"NOMBRE : {t[0]}\n CARGO : {t[1]}\n SUELDO BRUTO : {t[2]}\n DES. SALUD : {t[3]}\n DESC. AFP : {t[4]}\n SUELDO LIQUIDO : {t[5]}\n\n"
                    archivo.write(texto)
                
        else:
            with open("trabajadores_por_cargo.txt","w" , newline= "") as archivo:
                for t in trabajadores:
                    if opc2 == cargos[opc2 - 1]:
                        texto = f"NOMBRE : {t[0]}\n CARGO : {t[1]}\n SUELDO BRUTO : {t[2]}\n DES. SALUD : {t[3]}\n DESC. AFP : {t[4]}\n SUELDO LIQUIDO : {t[5]}\n\n"
                        archivo.write(texto)
        print("ARCHIVO CREADO CON EXITO")

def opcion_4():
    print("Hasta pronto!!")
    exit()