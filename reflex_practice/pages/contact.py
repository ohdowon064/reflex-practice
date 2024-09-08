import reflex as rx

from reflex_practice import navigation
from reflex_practice.ui.base import base_page


@rx.page(route=navigation.routes.CONTACT_ROUTE)
def contact_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Contact Us", size="9"),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id="my-child",
        )
    )
