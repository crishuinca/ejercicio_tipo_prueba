from funciones import *
import os, time, msvcrt


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
        opcion_1()
           
    elif opc == 2:
        opcion_2()
        
    elif opc== 3:
        opcion_3()

    else:
        opcion_4()
    time.sleep(3)