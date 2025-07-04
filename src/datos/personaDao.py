from src.datos.conexion import Conexion
from src.dominio.persona import Persona


class PersonaDao:
        _ERROR = -1
        _INSERT = ("insert into Persona(nombre,apellido, cedula, sexo, email) "
                  "Values (?,?,?,?,?)")
        @classmethod
        def insertar_persona(cls, persona):
            try:
                with Conexion.obtenerCursor() as cursor:
                    datos = (persona.nombre, persona.apellido,
                             persona.cedula, persona.sexo, persona.email)
                    registros = cursor.execute(cls._INSERT, datos)
                    print('Ejecuto')
                    return registros.rowcount

            except Exception as e:
                print(e)
                cursor.close()
                return cls._ERROR

if __name__ == '__main__':
    p = Persona('Fernando', 'Briones', '1317740981', 'M', 'fexchob4@mail.com')
    r = PersonaDao.insertar_persona(p)
    print (r)