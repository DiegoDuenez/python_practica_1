from Clases import Persona, Lista


salir = False
lista = Lista()
persona = Persona()

while True:
  
  print("- - - MENU PRINCIPAL - - -")
  print("(1) Persona que pidio material")
  print("(2) Persona que devolvio material")
  print("(3) Lista de pedidos")
  print("(4) Lista de entregas")
  print("(5) Salir")
  print("          ")
  mainMenu = int(input())
  print("          ")

  if mainMenu == 1:
    print("Ingrese el ID de la persona:")
    idNew = input()
    print("Ingrese el nombre de la persona:") 
    nombreNew = input()
    print("Ingrese el material que pidio:") 
    materialNew = input()
    print("Ingrese la fecha de pedido (DD/MM/AA):")
    fechaNew = input()
    fechaStr = str(fechaNew)
    print("          ")
    print("Atencion: La persona " + nombreNew + " pidió " + materialNew)
    print("          ")
    persona.pide(idNew, nombreNew, materialNew, fechaNew)
    salir = False

  if mainMenu == 2:
    print("Ingrese el ID de la persona:")
    idDev = input()
    print("Ingrese el nombre de la persona:") 
    nombre = input()
    print("Ingrese el material que devolvio:")
    material = input()
    print("Ingrese la fecha de devolucion (DD/MM/AA):")
    fecha = str(input())
    print("          ")
    print("Atencion: La persona " + nombre + " devolvio " + material)
    print("          ")
    persona.devuelve(idDev, nombre, material, fecha)
    
  if mainMenu == 3:
    lista.pedidos(True)
    salir = False

  if mainMenu == 4:
    lista.devoluciones(True)
    salir = False

  if mainMenu == 5:
    print("Has salido del sistema")
    salir = True
    
  if(salir == True):
        break


