from datetime import date, time
import reflex as rx
from typing import Optional
from sqlmodel import Field

class CalificadorDeEquipos(rx.Model, table=True):
    # Definimos el nombre exacto de la tabla si es diferente al de la clase
    __tablename__ = "calificador_de_equipo"

    # Campos de la tabla
    id: Optional[int] = Field(default=None, primary_key=True) # El ID es autoincremental por defecto
    container_number: Optional[str]
    code: Optional[str]
    description: Optional[str]

class Contenido_contenedores(rx.Model, table=True):
    # Definimos el nombre exacto de la tabla si es diferente al de la clase
    __tablename__ = "contenido_contenedor"

    # Campos de la tabla
    id: Optional[int] = Field(default=None, primary_key=True) # El ID es autoincremental por defecto
    code: Optional[int]
    description: Optional[str]

class EstatusContenedores(rx.Model, table=True):
    # Definimos el nombre exacto de la tabla si es diferente al de la clase
    __tablename__ = "estatus_contenedor"

    # Campos de la tabla
    id: Optional[int] = Field(default=None, primary_key=True) # El ID es autoincremental por defecto
    code: Optional[int]
    description: Optional[str]

class PuertosInternacionales(rx.Model, table=True):
    # Definimos el nombre exacto de la tabla si es diferente al de la clase
    __tablename__ = "puertosInternacionales"

    # Campos de la tabla
    id: Optional[int] = Field(default=None, primary_key=True) # El ID es autoincremental por defecto
    idpaises: Optional[int]
    codPaisPuerto: Optional[str]
    description: Optional[str]
    habilitadoPanama: Optional[bool]
    estado: Optional[bool]


class MovimientoContenedores(rx.Model, table=True):
    # Definimos el nombre exacto de la tabla si es diferente al de la clase
    __tablename__ = "movimiento_contenedores"

    # Campos de la tabla
    id: Optional[int] = Field(default=None, primary_key=True) # El ID es autoincremental por defecto
    operator: Optional[str] 
    trip_number: Optional[str]
    ship_name: Optional[str]
    loading_port: Optional[str]
    discharge_port: Optional[str]
    delivery_port: Optional[str]
    dock: Optional[int]
    arrival_date: Optional[date]
    arrival_time: Optional[time]
    departure_date: Optional[date]
    departure_time: Optional[time]
    container_number: Optional[str]
    size: Optional[int]
    type: Optional[int]
    status: Optional[int]
    full_empty: Optional[int]
    temperature: Optional[str]
    description: Optional[str]
    dgn_code: Optional[str]
    imo: Optional[int] # bigint se mapea como int en Python
    call_sign: Optional[str]
    visit_no: Optional[int]
    eqd_qual: Optional[str]
    port_register: Optional[str]