import reflex as rx
import pandas as pd

from sqlmodel import select, or_, func

# Modelos
from rx_infoport.models.container_movement_model import MovimientoContenedores

class ContainerMovementState(rx.State):
    # Estado para almacenar los movimientos de contenedores
    container_movements: list[MovimientoContenedores] = []
    columns: list[str] =[
        "Operador", 
        "No. Viaje", 
        "Nombre de la Nave", 
        "Puerto de Llegada", 
        "Puerto de Desembarque", 
        "Puerto de Entrega", 
        "Barco", 
        "Fecha de Llegada", 
        "Hora de Llegada", 
        "Fecha de Desembarque", 
        "Hora de Desembarque", 
        "No. Contenedor",
        "Tamaño", 
        "Tipo", 
        "Estatus", 
        "Lleno/Vacio", 
        "Temperatura", 
        "Descripción", 
        "DGN Code", 
        "IMO", 
        "Call Sign", 
        "No. Visita", 
        "EQD Qual", 
        "Registro de Puerto",
    ],

    def load_container_movements(self):
        # Cargar los movimientos de contenedores desde la base de datos
        with rx.session() as session:
            self.container_movements = session.exec(select(MovimientoContenedores)).all()

    @rx.var
    def dict_data(self) -> pd.DataFrame:
        # 1. Convertimos la lista de objetos de la base de datos a un DataFrame
        df = pd.DataFrame([item.dict() for item in self.container_movements])
        
        # 1. Diccionario de traducción (Mantenlo fuera o como constante para limpieza)
        nombres_espanol = {
            "operator": "Operador",
            "loading_port": "Pto. de Carga",
            "discharge_port": "Pto. de Descarga",
            "arrival_date": "Fch. de Llegada",
            "arrival_time": "Hr. de Llegada",
            "departure_date": "Fch. de Salida",
            "departure_time": "Hr. de Salida",
            "status": "Estatus",
            "full_empty": "Lleno/Vacio",
            "port_register": "Pto. de Registro",
            "ship_name": "Nombre Navio",
            "container_number": "No. de Contenedor",
            "size": "Tamaño",
            "type": "Tipo",
            "temperature": "Temperatura",
            "description": "Descripción",
            "dgn_code": "Cód. DGN",
            "imo": "IMO",
            "call_sign": "Letra Radio",
            "trip_number": "No. de Viaje",
            "delivery_port": "Pto. de Entrega",
            "dock": "Muelle",  
            "visit_no": "No. Visita",
            "eqd_qual": "EQD Qual",  
        }

        # 2. Definir el orden deseado (usando los nombres originales de la BD)
        cols_to_display = list(nombres_espanol.keys())
        
        # 3. VALIDACIÓN CRÍTICA: Si la lista está vacía, retornar DF con columnas pero sin filas
        if not self.container_movements:
            # Esto evita el KeyError al inicializar las columnas aunque no haya datos
            return pd.DataFrame(columns=list(nombres_espanol.values()))
        
        # 4. Construcción del DataFrame cuando ya hay datos
        df = pd.DataFrame([item.dict() for item in self.container_movements])

        # 5. Filtrar columnas, rellenar vacíos y renombrar
        # Usamos .reindex para que si falta alguna columna en los datos no explote
        df_display = df.reindex(columns=cols_to_display).fillna('')
        
        return df_display.rename(columns=nombres_espanol)