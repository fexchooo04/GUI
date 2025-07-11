from src.datos.conexion import Conexion
from src.dominio.persona import Persona


class PersonaDao:
    _ERROR = -1
    _INSERT = ("insert into Persona(nombre, apellido, cedula, sexo, email) "
               "VALUES (?,?,?,?,?)")
    _SELECT = ("SELECT nombre, apellido, cedula, sexo, email FROM Persona "
               "where cedula=?")
    _UPDATE = ("update Persona set nombre=?, apellido=?, sexo=?, email=? "
               "where cedula=?")
    _DELETE = "delete from Persona where cedula=?"

    @classmethod
    def insertar_persona(cls, persona):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (persona.nombre, persona.apellido,
                         persona.cedula, persona.sexo, persona.email,)
                registros = cursor.execute(cls._INSERT, datos)
                return registros.rowcount
        except Exception as e:
            print(f"Error al insertar persona: {e}")
            cursor.rollback()
            return cls._ERROR

    @classmethod
    def seleccionar_persona(cls, cedula):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (cedula,)
                registro = cursor.execute(cls._SELECT, datos).fetchone()
                print(registro)
                if registro[3] == 'M':
                    sexo =  'Masculino'
                else:
                    sexo = 'Femenino'
                persona = Persona(nombre=registro[0],
                                  apellido=registro[1],
                                  cedula=registro[2],
                                  email=registro[4],
                                  sexo=sexo)
                return persona
        except Exception as e:
            print(f"Error al consultar persona: {e}")
            return None

    @classmethod
    def actualizar_persona(cls, persona):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (persona.nombre, persona.apellido,
                         persona.sexo, persona.email, persona.cedula,)
                registros = cursor.execute(cls._UPDATE, datos)
                return registros.rowcount
        except Exception as e:
            print(f"Error al actualizar persona: {e}")
            cursor.rollback()
            return cls._ERROR

    @classmethod
    def eliminar_persona(cls, cedula):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (cedula,)
                registros = cursor.execute(cls._DELETE, datos)
                return registros.rowcount
        except Exception as e:
            print(f"Error al eliminar a la persona: {e}")
            cursor.rollback()
            return cls._ERROR

if __name__ == '__main__':
    p = Persona('Jose', 'Perez', '0123456789', 'M', 'lperez@mail.com')
    # r = PersonaDao.insertar_persona(p)
    r = PersonaDao.actualizar_persona(p)
    print(r)