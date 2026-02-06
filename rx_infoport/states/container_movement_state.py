import reflex as rx
from sqlmodel import select, or_, func

# Modelos
from rx_infoport.models.container_movement_model import MovimientoContenedores

class ContainerMovementState(rx.State):
    # Estado para almacenar los movimientos de contenedores
    container_movements: list[MovimientoContenedores] = []

    def load_container_movements(self):
        # Cargar los movimientos de contenedores desde la base de datos
        with rx.session() as session:
            self.container_movements = session.exec(select(MovimientoContenedores)).all()