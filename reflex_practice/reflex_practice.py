import reflex as rx

from reflex_practice.pages.about import about_page
from reflex_practice.pages.pricing import pricing_page
from reflex_practice.ui.base import base_page
from rxconfig import config


class State(rx.State):
    label = "Welcome to Reflex!"

    def on_change(self, value: str) -> None:
        self.label = value

    def on_click(self):
        print("label clicked!")


def index() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading(State.label, size="9"),
            rx.text(
                "Let's build something cool with Reflex! ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.input(
                default_value=State.label,
                on_click=State.on_click,
                on_change=State.on_change,
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id="my-child",
        )
    )


app = rx.App()
app.add_page(index)
app.add_page(about_page, "/about")
app.add_page(pricing_page, "/pricing")
