from empleado import Empleado
from marcacion import MarcacionTipo
from marcacion import Marcacion
from marcacionAdminAbstracta import MarcacionesAdminAbstract

class MarcacionAdmin(MarcacionesAdminAbstract):

    def agregar(self, marcacion: Marcacion) -> None:
        self.marcaciones.append(marcacion)

    def empleados(self) -> list:
        setEmpleados = set()
        for marcacion in self.marcaciones:
            setEmpleados.add(marcacion.empleado)
        return list(setEmpleados)

    def filtrar_por_empleado(self, empleado: Empleado) -> list:
        lista = []
        for marcacion in self.marcaciones:
            if marcacion.empleado == empleado:
                lista.append(marcacion)
        return lista

    def filtrar_por_tipo(self, tipo: Marcacion) -> list:
        lista = []
        for marcacion in self.marcaciones:
            if marcacion.tipo == tipo:
                lista.append(marcacion)
        return lista
    
    def llegadas_tarde(self) -> list:
        lista = []
        for marcacion in self.marcaciones:
            if marcacion.tipo == MarcacionTipo.ENTRADA.name:
                if marcacion.fecha_hora.time() > marcacion.empleado.oficina.hora_entrada:
                    lista.append(marcacion)
        return lista
    
    def ordenar_legajo(self) -> None:
        self.marcaciones = sorted(self.marcaciones, key = lambda obj: (obj.empleado.legajo, obj.fecha_hora))
    
    def ordenar_apellido_nombre(self) -> None:
        self.marcaciones = sorted(self.marcaciones, key = lambda obj: (obj.empleado.apellido, obj.empleado.nombre, obj.fecha_hora))