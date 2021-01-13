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
    

