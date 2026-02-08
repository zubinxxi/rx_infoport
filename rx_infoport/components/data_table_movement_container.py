import reflex as rx
import pandas as pd


# State
from rx_infoport.states.container_movement_state import ContainerMovementState

# Model
from rx_infoport.models.container_movement_model import MovimientoContenedores


def data_table() -> rx.Component:
    return rx.vstack(
        rx.heading("Movimientos de Contenedores", size="7"),
        rx.data_table(
            data=ContainerMovementState.dict_data,
            pagination=True, # Habilita paginación [p. ej. en componentes de datos]
            search=True,     # Agrega buscador tipo Select2 incorporado
            sort=True,       # Permite ordenar columnas
            resizable=True,  # Permite que las columnas se ajusten y redimensionen
        ),
        # Ejecuta la carga de datos al montar la página [5]
        on_mount=ContainerMovementState.load_container_movements,
        padding="2em",
        width="100%",
    )