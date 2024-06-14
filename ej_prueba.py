import os
import msvcrt
import time

trabajadores = []

os.system("cls")
print(" Bienvenido a la plantilla de trabajadores")
print("<<Presione una tecla para continuar>>")
msvcrt.getch()

while True:
    os.system("cls")
   
    print("""              MENÚ
#########################################
1) Registrar trabajador 
2) Listar todos los trabajadores
3) Imprimir plantilla de sueldos
4) Salir del programa
#########################################""")
    try:
         opc = int(input("Seleccione la opción deseada: "))
         if opc in (1,2,3,4):
             pass
         
    except:
        print("La opción es invalida")
     
    if opc == 1:
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
        trabajador = [nombre_apellido , cargo , sueldo_bruto ,desc_afp , desc_salud , sueldo_liquido]
        trabajadores.append(trabajador)
        print("TRABAJADOR REGISTRADO CON EXITO!")    

    elif opc == 2:
        if len(trabajadores) == 0:
            print("No existen trabajadores, elija la opción 1")
        else:
            print("\tLista de trabajadores")
            print("Trabajador \tCargo \tSueldo Bruto \tDes. Salud \t Des. AFP \tLiquido a pagar")
            for t in trabajadores:  # t seria cada trabajador de la lista, t es una lista dentro de otra lista
                
                for x in range(6):
                    print(f"{t[0]}\t{t[1]}\t\t{t[2]}\t\t{t[3]}\t\t{t[4]}\t\t{t[5]}")

    elif opc== 3:
        pass
    elif opc == 4:
        print("Hasta pronto!!")
        time.sleep(1)
        break
    else:
        print("La opción elegida no esta en el menú")
        time.sleep(1.5)
    time.sleep(3)