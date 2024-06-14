import os
import msvcrt
import time

trabajadores = []
Cargos = []
S_bruto = []
Desc_salud = []
Desc_AFP = []
S_liquido = []


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
        
        while True:
            nombre= input("Ingrese el nombre y apellido del trabajador: ")
            if nombre not in trabajadores:
                trabajadores.append(nombre)
                break
            elif nombre in trabajadores:
                print(" El nombre ya se encuentra registrado")
                time .sleep (2)

        while True:
            cargo=input("Ingrese el cargo del trabajador: ").lower
            if cargo == "ceo" or "desarrollador" or "analista de datos":
                Cargos.append(cargo)
                break
            else:
                print ("No esta")
        
        while True:
            s_brut = float(input("Ingresa el sueldo bruto del trabajador: "))
            if s_brut <= 0:
                print("El sueldo no puede ser $0") 
            elif s_brut > 0:
               S_bruto.append(s_brut)
               break
        brut = [s_brut * 0.07]
        print(f"El descuento de 7% en salud es: {brut[0]}")
        time.sleep(2)
        
        AFP= int(input(" Ingrese porcentaje de AFP (entre 7% y 12%): "))
        print(f"")
        



        



            
    

    elif opc == 2:

        pass
    elif opc== 3:
        pass
    elif opc == 4:
        print("Hasta pronto!!")
        time.sleep(1)
        break
    else:
        print("La opción elegida no esta en el menú")
        time.sleep(1.5)