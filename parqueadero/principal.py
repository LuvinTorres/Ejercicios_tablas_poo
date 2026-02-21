from modelo_usuario import Usuario
from carro import Carro
from parqueadero import Parqueadero

print("\n-------------DATOS DEL CLIENTE-----------\n")

nombre = input("ingrese su nombre: ")
cedula = input("ingrese su numero de cedula: ")
tipo_usuario = input("que tipo de usuario es: ")
obj_usuario1= Usuario(nombre, cedula , tipo_usuario)

print("\n-------INFORMACION DEL VEHICULO---------\n")

placa = input("ingrese su placa: ")
cedula = input("ingrese la marca del carro: ")
color = input("ingrese el color del carro: ")
obj_carro1= Carro(placa, cedula, color)

print("\n------------PARQUEADERO------------------\n")

puesto= input("ingrese el puesto asignado: ")
fecha= input("ingrese la fecha de hoy: ")
obj_parqueadero= Parqueadero(puesto,fecha)
obj_parqueadero.registrar_entrada()
obj_parqueadero.registrar_salida()

print("\n")

obj_parqueadero.guardar_info()
obj_usuario1.mostrar_info()
obj_carro1.mostrar_info()
obj_parqueadero.mostrar_info()

