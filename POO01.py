class Persona:
    def __init__(self,nombre,edad,genero):
        self.nombre = nombre #'Adonay'
        self.edad = edad #33
        self.genero = genero #False
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre = nombre
    def getGenero(self):
        return self.genero
    def setGenero(self,genero):
        self.genero = genero
    def getEdad(self):
        return self.edad
    def setEdad(self,b):
        self.edad = b

class Profesional(Persona):
    def __init__(self,nombre,edad,genero,profesion):
        Persona.__init__(self,nombre,edad,genero)
        self.profesion = profesion
    def getProfesion(self):
        return self.profesion

class Empresa():
    def __init__(self,nombre,gerente):
        self.nombre = nombre
        self.gerente = gerente
        self.empleados = []
    def getNombre(self):
        return self.nombre
    def getGerente(self):
        return self.gerente
    def getEmpleado(self,indice):
        return self.empleados[indice]
    def getNumEmp(self):
        return len(self.empleados)
    def setEmpleado(self,empleado):
        self.empleados.append(empleado)

print('***Persona***')
Per01 = Persona('Felipe',45,False)
Per02 = Persona('Ana',25,True)
print(Per01.getNombre())
print(Per01.getEdad())
print(Per01.getGenero())
print('***Profesional***')
Pro01 = Profesional('Luisa',30,True,'ICG')
print(Pro01.getProfesion())
print(Pro01.getNombre())
print(Pro01.getEdad())
print(Pro01.getGenero())
print('***Empresa***')
Emp01 = Empresa('ICG S.A.',Pro01)
print('Empresa: ' + Emp01.getNombre())
print('nombre del gerente: '+ Emp01.getGerente().getNombre())
print('num empleados: '+ str(Emp01.getNumEmp()))
Emp01.setEmpleado(Per01)
Emp01.setEmpleado(Per02)
print('num empleados: '+ str(Emp01.getNumEmp()))
print('num empleados: '+ Emp01.getEmpleado(1).getNombre())
