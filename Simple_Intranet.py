# idea general: Crear un servicio de intranet para uso de profesores y alumnos
import json
def cargar_usuarios():
    with open("usuarios.json", "r") as file:
        usuarios = json.load(file)
    return usuarios
usuarios = cargar_usuarios()
class Usuario:
    def __init__(self, matricula, password):
        self.matricula = matricula
        self.password = password
    def login(self, matricula, password):
        for u in usuarios:
            if matricula == u['matricula'] and password == u['password']:
                return True
            else:
                return False
    def logout(self):
        print("[\033[32m*\o33[0m] Sesion cerrada") 
        # \033[32m es para cambiar el color de la letra a verde
        # \033[0m es para volver al color default
        # porque? porque se ve bonito :D
# Los profesores podran crear, modificar y eliminar alumnos, asi como tambien crear, modificar y eliminar notas
# Ademas, podran ver el listado de alumnos y sus notas, asi como tambien el promedio de cada uno
class Profesor(Usuario):
    def __init__(self, matricula, password):
        super().__init__(matricula, password)
    def cambiar_nota(Alumno):
        pass
class Alumno(Usuario):
    def __init__(self, matricula, password):
        super().__init__(matricula, password)
        self.ramos = []
        self.ramos_botados = []
    def inscribir_ramo(self, ramo):
        self.ramos.append(ramo)
        return "[\033[32m*\033[0m] Ramo inscrito correctamente"
    def botar_ramo(self, ramo):
        print("Ramos inscritos: ")
        self.mostrar_ramos()
        if ramo in self.ramos:
            self.ramos_botados.append(ramo)
            self.ramos.remove(ramo)
            return "[\033[32m*\033[0m] Ramo botado"
    def mostrar_ramos(self):
        for ramo in self.ramos:
            print(ramo)
    def __str__(self):
        return f"""
        Nombre: {self.nombre}
        Apellido: {self.apellido}
        Matricula: {self.matricula}
        Password: {self.password}
        """
class Root(Usuario):
    def __init__(self, matricula, password, rol):
        super().__init__(matricula, password)
        def crear_usuario(self, matricula, password):
            usuarios.append({"matricula": matricula, "password": password})
            with open("usuarios.json", "w") as file:
                json.dump(usuarios, file)
class Ramo:
    def __init__(self, nombre, codigo, modulo, usuario):
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
    def __str__(self): # __str__ es un metodo especial que se ejecuta cuando se llama a print
        return f"""
        Nombre: {self.nombre}
        Codigo: {self.codigo}
        """
    def get_ramo():
        print(str(self))
def main():
    print("""Bienvenido a intranet
          \x1B[34mIniciar sesion\x1B[0m
          """)
    matricula = input("Matricula: ")
    password = input("Clave: ")
    #user = Usuario(matricula, password)
    #if user.login(matricula, password):
        # verificar si es profesor o alumno

