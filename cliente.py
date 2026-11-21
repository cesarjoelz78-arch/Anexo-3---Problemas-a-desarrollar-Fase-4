import re
from entidad import Entidad
from excepción import DatosInvalidosError


class Cliente(Entidad):
    def __init__(self, identificacion, nombre, correo, telefono):
        super().__init__(identificacion)
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise DatosInvalidosError("El nombre es obligatorio")
        self.__nombre = valor.strip()

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        if not isinstance(valor, str):
            raise DatosInvalidosError("El correo debe ser texto")

        valor = valor.strip()
        patron = r"^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$"

        if not re.match(patron, valor):
            raise DatosInvalidosError("El correo electrónico no es válido")

        self.__correo = valor

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        if not isinstance(valor, str):
            raise DatosInvalidosError("El teléfono debe ser texto")

        valor = valor.strip()

        if not valor.isdigit() or not 7 <= len(valor) <= 15:
            raise DatosInvalidosError(
                "El teléfono debe contener entre 7 y 15 dígitos"
            )

        self.__telefono = valor

    def mostrar_informacion(self):
        return (
            f"Cliente: {self.nombre}\n"
            f"Identificación: {self.identificacion}\n"
            f"Correo: {self.correo}\n"
            f"Teléfono: {self.telefono}"
        )
