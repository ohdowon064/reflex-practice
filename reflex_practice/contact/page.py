import reflex as rx

from reflex_practice.contact.form import contact_form
from reflex_practice.contact.model import ContactModel
from reflex_practice.contact.state import ContactState
from reflex_practice.ui.base import base_page


def contact_page(contact: ContactModel) -> rx.Component:
    return rx.box(
        rx.heading(contact.first_name),
        rx.text(contact.message),
        padding="1em",
    )


def contacts_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Contact List", size="9"),
            rx.foreach(
                iterable=ContactState.contacts,
                render_fn=contact_page,
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
        )
    )


def create_contact_page() -> rx.Component:
    my_child = rx.vstack(
        rx.heading("Contact Us", size="9"),
        rx.cond(
            condition=ContactState.did_submit,
            c1=ContactState.thank_you,
            c2="",
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
