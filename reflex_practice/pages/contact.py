import reflex as rx

from reflex_practice import navigation
from reflex_practice.contact.form import contact_form
from reflex_practice.contact.state import ContactState
from reflex_practice.ui.base import base_page


@rx.page(
    route=navigation.routes.CONTACT_ROUTE,
    on_load=ContactState.start_timer,
)
def contact_page() -> rx.Component:
    my_child = rx.vstack(
        rx.heading("Contact Us", size="9"),
        rx.text(ContactState.timeleft_label),
        rx.cond(
            ContactState.did_submit,
            ContactState.thank_you,
            "",
        ),
        rx.desktop_only(
            rx.box(
                contact_form(),
                id="my-form-box",
                width="50vw",
            )
        ),
        rx.tablet_only(
            rx.box(
                contact_form(),
                id="my-form-box",
                width="75vw",
            )
        ),
        rx.mobile_only(
            rx.box(
                contact_form(),
                id="my-form-box",
                width="85vw",
            )
        ),
        spacing="5",
        justify="center",
        align="center",
        min_height="85vh",
        id="my-child",
    )
    return base_page(my_child)
