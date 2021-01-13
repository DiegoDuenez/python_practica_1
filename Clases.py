registroPedir = {}
registroDev = {}


class Persona:
    
  def pide(self, idPersona, nombre,material, fecha):
    registroPedir.update({'Id_'+ repr(idPersona): repr(idPersona)})
    registroPedir.update({'Persona '+ repr(idPersona):nombre})
    registroPedir.update({'Material '+ repr(idPersona):material
    })
    registroPedir.update({'Fecha pedido '+ repr(idPersona):fecha})

  def devuelve(self, idPersona, nombre, material, fecha):
    registroPedir.pop('Id_'+ repr(idPersona))
    registroPedir.pop('Persona '+ repr(idPersona))
    registroPedir.pop('Material '+ repr(idPersona))
    registroPedir.pop('Fecha pedido '+ repr(idPersona))
    registroDev.update({'Id_'+ repr(idPersona): repr(idPersona)})
    registroDev.update({'Persona '+ repr(idPersona):nombre})
    registroDev.update({'Material '+ repr(idPersona):material})
    registroDev.update({'Fecha devolucion '+ repr(idPersona):fecha})
  
      
class Lista:

  def pedidos(self, activar):
    self.activar = activar
    if activar == True:
      print("- - - LISTA DE PERSONAS QUE PIDIERON - - -")
      for value in registroPedir:
        valor = registroPedir[value]
        print(value + ": " + valor)
      print("- - - - - - - - - - - - - - - - - - - - - -")
      print("          ")  

  def devoluciones(self, activar):
    self.activar = activar
    if activar == True:
      print("- - - LISTA DE PERSONAS QUE DEVOLVIERON - - -")
      for value in registroDev:
        valor = registroDev[value]
        print(value + ": " + valor)
      print("- - - - - - - - - - - - - - - - - - - - - - -")
      print("          ")
    

class Menu:

  def principal(self):
    print("- - - MENU PRINCIPAL - - -")
    print("(1) Persona que pidio material")
    print("(2) Persona que devolvio material")
    print("(3) Lista de pedidos")
    print("(4) Lista de entregas")
    print("(5) Salir")
    print("          ")

  
  def pedido(self, persona = Persona()):
    print("Ingrese el ID de la persona:")
    idNew = input()
    print("Ingrese el nombre de la persona:") 
    nombreNew = input()
    print("Ingrese el material que pidio:") 
    materialNew = input()
    print("Ingrese la fecha de pedido (DD/MM/AA):")
    fechaNew = input()
    print("          ")
    print("Atencion: La persona " + nombreNew + " pidió " + materialNew)
    print("          ")
    persona.pide(idNew, nombreNew, materialNew, fechaNew)

  def devolucion(self, persona = Persona()):
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