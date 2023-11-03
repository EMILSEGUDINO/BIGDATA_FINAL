import json
import os
import pathlib

class Persona:

    AGREGAR_PERSONA = 1
    CONSULTAR_PERSONA = 2
    SALIR = 0

    def __init__(self):
        self._Personas = []
        self.consultar_personas('BASE.json')

    def __del__(self):
        self.agregar_persona('BASE.json')

    @property
    def personas(self):
        return self._Personas

    def agregar_persona(self, ruta):
        with open(ruta, 'w') as archivo:
            json.dump({'Personas': [p.__dict__ for p in self.personas]}, archivo, cls=Base_Encoder, indent=4)

    def consultar_personas(self, ruta):
        if pathlib.Path(ruta).exists():
            with open(ruta, 'r') as archivo:
                datos = json.load(archivo)
                for persona in datos['Personas']:
                    self.personas.append(desde_json(persona))

    def menu(self):
        continuar = True
        while continuar:
            os.system('cls')
            print(f'''          Base
    {self.AGREGAR_PERSONA})           Agregar Datos
    {self.CONSULTAR_PERSONA})          Consultar
    {self.SALIR})         SALIR''')
            opc = input('Seleccionar una opcion: ')
            try:
                opc = int(opc)
            except ValueError:
                opc = -1
            if opc == self.AGREGAR_PERSONA:
                self.agregar_persona()
            elif opc == self.CONSULTAR_PERSONA:
                self.consultar_personas()
            elif opc == self.SALIR:
                continuar = False
            else:
                os.system('cls')
                print('Opción no válida')
                input('Presiona Enter para continuar')

        input('Presiona enter para Salir')


class Base_Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Persona):
            return {'nombre': obj.nombre, 'edad': obj.edad, 'ciudad': obj.ciudad, 'fecha_nacimiento': obj.fecha_nacimiento}
        return json.JSONEncoder.default(self, obj)


def desde_json(diccionario):
    return Persona(diccionario['nombre'], diccionario['edad'], diccionario['ciudad'], diccionario['fecha_nacimiento'])


if __name__ == '__main__':
    p = Persona()
    p.menu()
