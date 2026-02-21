from modelo_usuario import Usuario
from modelo_numero import Numero
from modelo_calculadora import Calculadora

# Crear usuario
nombre = input("Ingrese su nombre: ")
id_usuario = input("Ingrese su id: ")
usuario1 = Usuario(nombre, id_usuario)

# Crear números
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))

obj_num1 = Numero(num1)
obj_num2 = Numero(num2)

# Crear calculadora
obj_calculadora = Calculadora("17/02/2026")

# Pedir tipo de operación
obj_calculadora.operacion = input(
    "Ingrese el tipo de operacion (suma, resta, multiplicar, dividir): "
).lower()

# Hacer operación
resultado = obj_calculadora.hacer_operaciones(obj_num1, obj_num2)

print("Resultado:", resultado)

# Guardar información del usuario
info=obj_calculadora.guardar_info(usuario1)

# Mostrar tabla
obj_calculadora.mostrar_tabla()