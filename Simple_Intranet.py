# idea general: Crear un servicio de intranet para uso de profesores y alumnos

class Intranet:
    def __init__(self, usuarios):
        self.usuarios = usuarios

    def login(self, matricula, password):
        for u in usuarios:
            if matricula == usuario['matricula'] and password == usuario['password']:
                return True
            else:
                return False
    def logout(self):
        print("Saliendo...")
        main()
# Los profesores podran crear, modificar y eliminar alumnos, asi como tambien crear, modificar y eliminar notas
# Ademas, podran ver el listado de alumnos y sus notas, asi como tambien el promedio de cada uno
class Profesor(Intranet):
    def __init__(self, nombre, matricula, password, usuarios):
        super().__init__(usuarios)
        self.nombre = nombre
        self.matricula = matricula
        self.password = password
    def cambiar_nota(Alumno)
class Alumno(Intranet):
    self.ramos = []
    def __init__(self, nombre, apellido, matricula, email, password):
        super().__init__(nombre, apellido, matricula, email, password)
    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nMatricula: {self.matricula}\nEmail: {self.email}\nPassword: {self.password}"

class Ramo):
    def __init__(self, nombre, codigo, modulo, profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.modulo = modulo
        self.notas = []
    def calcular_promedio(self):
        suma = 0
        if len(self.notas) != 0:
            for nota in self.notas:
                suma += nota
            return suma / len(self.notas)
        if 
    def __str__(self): # __str__ es un metodo especial que se ejecuta cuando se llama a print
        return f"""
        Nombre: {self.nombre}
        Codigo: {self.codigo}
        """
    def get_ramo():
        print(str(self))
def main():
    print("Bienvenido a intranet")

