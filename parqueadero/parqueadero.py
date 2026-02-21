class Parqueadero:

    def __init__(self, puesto, fecha_entrada):
        self.puesto = puesto
        self.fecha_entrada = fecha_entrada
        self.hora_entrada = ""
        self.hora_salida = ""
        self.estado = ""
        self.texto_tabla= ""

    def registrar_entrada(self):
        self.hora_entrada = input("Ingrese la hora de entrada: ")
        self.estado = "= Ocupado"
   
    def registrar_salida(self):
        self.hora_salida = input("Ingrese la hora de salida: ").strip()
    
        if self.hora_salida == "":
          self.estado = "Ocupado"
        else:
          self.estado = "Disponible"


    def guardar_info(self):
       self.texto_tabla = self.texto_tabla + f" -Puesto: {self.puesto} ,-Fecha entrada: {self.fecha_entrada} , -Hora entrada: {self.hora_entrada}, -Hora salida: {self.hora_salida}, -Estado: {self.estado}"

    def mostrar_info(self):
       print (self.texto_tabla)