from src.datos.conexion import Conexion
from src.dominio.persona import Persona


class PersonaDao:
        _ERROR = -1
        _INSERT = ("insert into Persona(nombre,apellido, cedula, sexo, email) "
                  "Values (?,?,?,?,?)")
        _SELECT = ("SELECT nombre, apellido, apellido, cedula, sexo, email FROM Persona "
                   "where cedula = ?")


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


        @classmethod
        def seleccionar_persona(cls, cedula):
            try:
                with Conexion.obtenerCursor() as cursor:
                    datos = (cedula,)
                    registros = cursor.execute(cls._SELECT, datos)
                    persona = Persona(nombre=registros.fetchone()[0],
                                      apellido=registros.fetchone()[1],
                                      cedula=registros.fetchone()[2],
                                      sexo=registros.fetchone()[3],
                                      email=registros.fetchone()[4])
                    return persona



            except Exception as e:
                print(e)
                cursor.rollback()
                return cls._ERROR

if __name__ == '__main__':
    #p = Persona('Fernando', 'Briones', '1317740981', 'M', 'fexchob4@mail.com')
    #r = PersonaDao.insertar_persona(p)
    r= PersonaDao.seleccionar_persona('1317740981')
    print (r)