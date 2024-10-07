import reflex as rx
from reflex_local_auth import RegistrationState, LoginState
from reflex_local_auth.pages.components import PADDING_TOP
from reflex_local_auth.pages.login import login_form
from reflex_local_auth.pages.registration import register_form

from reflex_practice.ui.base import base_page


def my_login_page() -> rx.Component:
    return base_page(
        rx.center(
            rx.cond(
                LoginState.is_hydrated,  # type: ignore
                rx.card(login_form()),
            ),
            padding_top=PADDING_TOP,
            min_height="80vh",
        )
    )


def my_register_page() -> rx.Component:
    return base_page(
        rx.center(
            rx.cond(
                RegistrationState.success,
                rx.vstack(
                    rx.text("Registration successful!"),
                ),
                rx.card(register_form()),
            ),
            padding_top=PADDING_TOP,
            min_height="80vh",
        )
    )
