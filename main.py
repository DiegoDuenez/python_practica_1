from Clases import Persona, Lista, Menu

salir = False
lista = Lista()
persona = Persona()
menu = Menu()

while True:
  
  menu.principal()
  mainMenu = int(input())
  
  if mainMenu == 1:
    menu.pedido()
    salir = False

  if mainMenu == 2:
    menu.devolucion()
    salir = False
    
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


