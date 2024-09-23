
class Persona:
    def __init__(self,nombre,edad,genero):
        self.__nombre = nombre #'Andi'
        self.__edad = edad #32
        self.__genero = genero #True
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre = nombre
    def getEdad(self):
        return self.__edad
    def getGenero(self):
        return self.__genero

class Profesional(Persona):
    def __init__(self,nombre,edad,genero,titulo):
        self.__titulo = titulo
        Persona.__init__(self,nombre,edad,genero)
    def getTitulo(self):
        return self.__titulo    

class Empresa:
    def __init__(self,nombre, gerente):
        self.__nombre = nombre    
        self.__gerente = gerente
        self.__empleados = []
    def getNombre(self):
        return self.__nombre    
    def getGerente(self):
        return self.__gerente
    def getNumEmpleados(self):
        return len(self.__empleados)
    def getEmpleado(self,indice):
        return self.__empleados[indice]
    def setEmpleado(self,empleado):
        self.__empleados.append(empleado)

print("-----PERSONAS-----")
Per01 = Persona("Javier",48,False) #instancia de la clase Persona
print(Per01.getNombre(),Per01.getEdad(),Per01.getGenero())
#Per01.setNombre("Tony")
#Per01._Persona__nombre="Adonay"
Per02 = Persona("Ana",24,True)
print(Per02.getNombre(),Per02.getEdad(),Per02.getGenero())
Per03 = Persona("Matias",34,False)
print(Per03.getNombre(),Per03.getEdad(),Per03.getGenero())
print()
print("-----PROFESIONAL-----")
Pro01 = Profesional("Maria",24,True,"ICG")
print(Pro01.getNombre(),Pro01.getEdad(),Pro01.getGenero(),Pro01.getTitulo())
print()
print("-----EMPRESA-----")
Emp01 = Empresa("ICG S.A.", Pro01)
print("nombre", Emp01.getNombre())
print("nombre gerente", Emp01.getGerente().getNombre())
print("profesion gerente", Emp01.getGerente().getTitulo())
print("num empl",Emp01.getNumEmpleados())
Emp01.setEmpleado(Per01)
Emp01.setEmpleado(Per02)
Emp01.setEmpleado(Per03)
print("num empl",Emp01.getNumEmpleados())
print("nombre empleado 1", Emp01.getEmpleado(0).getNombre())
print("nombre empleado 2", Emp01.getEmpleado(1).getNombre())