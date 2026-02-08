import reflex as rx

# State
from rx_infoport.states.container_movement_state import ContainerMovementState

# Model
from rx_infoport.models.container_movement_model import MovimientoContenedores


def show_container_movements(index: int, movement: MovimientoContenedores) -> rx.Component:
    return rx.table.row(
        rx.table.cell(index + 1, align="center"),
        rx.table.cell(movement.operator, align="center"),
        rx.table.cell(movement.trip_number, align="center"),
        rx.table.cell(movement.ship_name, align="center"),
        rx.table.cell(movement.loading_port, align="center"),
        rx.table.cell(movement.discharge_port, align="center"),
        rx.table.cell(movement.delivery_port, align="center"),
        rx.table.cell(movement.dock, align="center"),
        rx.table.cell(movement.arrival_date, align="center"),
        rx.table.cell(movement.arrival_time, align="center"),
        rx.table.cell(movement.departure_date, align="center"),
        rx.table.cell(movement.departure_time, align="center"),
        rx.table.cell(movement.container_number, align="center"),
        rx.table.cell(movement.size, align="center"),
        rx.table.cell(movement.type, align="center"),
        rx.table.cell(movement.status, align="center"),
        rx.table.cell(movement.full_empty, align="center"),
        rx.table.cell(movement.temperature, align="center"),
        rx.table.cell(movement.description, align="center"),
        rx.table.cell(movement.dgn_code, align="center"),
        rx.table.cell(movement.imo, align="center"),
        rx.table.cell(movement.call_sign, align="center"),
        rx.table.cell(movement.visit_no, align="center"),
        rx.table.cell(movement.eqd_qual, align="center"),
        rx.table.cell(movement.port_register, align="center"),
        align="center",
        style={"_hover": {"bg": rx.color("gray", 3)}},
    )

def loading_table_movements() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.heading("Movimientos de Contenedores", size="7"),
            align="center",
            justify="start",
            width="100%",
        ),
        
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("No."),
                    rx.table.column_header_cell("Operador"),
                    rx.table.column_header_cell("No. Viaje"),
                    rx.table.column_header_cell("Nombre de la Nave"),
                    rx.table.column_header_cell("Puerto de Llegada"),
                    rx.table.column_header_cell("Puerto de Desembarque"),
                    rx.table.column_header_cell("Puerto de Entrega"),
                    rx.table.column_header_cell("Barco"),
                    rx.table.column_header_cell("Fecha de Llegada"),
                    rx.table.column_header_cell("Hora de Llegada"),
                    rx.table.column_header_cell("Fecha de Desembarque"),
                    rx.table.column_header_cell("Hora de Desembarque"),
                    rx.table.column_header_cell("No. Contenedor"),
                    rx.table.column_header_cell("Tamaño"),
                    rx.table.column_header_cell("Tipo"),
                    rx.table.column_header_cell("Estatus"),
                    rx.table.column_header_cell("Lleno/Vacio"),
                    rx.table.column_header_cell("Temperatura"),
                    rx.table.column_header_cell("Descripción"),
                    rx.table.column_header_cell("DGN Code"),
                    rx.table.column_header_cell("IMO"),
                    rx.table.column_header_cell("Call Sign"),
                    rx.table.column_header_cell("No. Visita"),
                    rx.table.column_header_cell("EQD Qual"),
                    rx.table.column_header_cell("Registro de Puerto"),
                ),
            ),

            rx.table.body(
                rx.foreach(
                    ContainerMovementState.container_movements, 
                    lambda movement, index: show_container_movements(index, movement),
                ),
                
            ),
            on_mount=ContainerMovementState.load_container_movements,
            variant="surface",
            size="3",
            #margin_top="20px",
            width="100%",
            min_heigth="50vh",
            border_radius="lg",
            overflow="hidden",
        ),
        width="100%",
        overflow_y="auto",
        padding="4%",
        align="center",
        justify="center",
    )
        
    
