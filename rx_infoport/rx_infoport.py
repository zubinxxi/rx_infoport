"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
# State
#from .states.container_movement_state import ContainerMovementState

# Components
from .components.container_movement_componet import loading_table_movements
from .components.data_table_movement_container import data_table


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.vstack(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading(
                "🚢 Dashboard Interactivo: Movimiento de Contenedores", 
                size="9",
            ),
            rx.text(
                "Filtra los datos usando la barra lateral izquierda y observa las métricas clave.",
                size="5",
            ),
            rx.divider(),
            rx.spacer(),
            loading_table_movements(),
            #data_table(),
            #spacing="5",
            justify="center",
            #min_height="50vh",
            padding_top="2%",
            width="100%",
        ),
        width="100%",
    )


app = rx.App(
    theme=rx.theme( 
        has_background=True, 
        radius="small", 
        accent_color="cyan",
    ),
    stylesheets=[
        "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
        "https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,200..1000;1,200..1000&family=Raleway:ital,wght@0,100..900;1,100..900&family=Staatliches&display=swap",
    ],
)
app.add_page(index)
