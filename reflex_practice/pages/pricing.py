import reflex as rx

from reflex_practice.ui.base import base_page


def pricing_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Pricing", size="9"),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id="my-child",
        )
    )