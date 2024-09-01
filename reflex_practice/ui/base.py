import reflex as rx

from reflex_practice.ui.nav import navbar


def base_page(
    child: rx.Component,
    hide_navbar: bool = False,
    *args: tuple[...],
    **kwargs: dict[...],
) -> rx.Component:
    if not isinstance(child, rx.Component):
        child = rx.heading("this is not a valid child element.")

    if hide_navbar:
        return rx.container(
            child,
            rx.logo(),
            rx.color_mode.button(position="bottom-left"),
        )

    return rx.container(
        navbar(),
        child,
        rx.logo(),
        rx.color_mode.button(position="bottom-left"),
    )
