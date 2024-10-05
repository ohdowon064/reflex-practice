import reflex as rx

from reflex_practice import navigation
from reflex_practice.contact.form import contact_form
from reflex_practice.contact.model import ContactModel
from reflex_practice.contact.state import ContactState
from reflex_practice.ui.base import base_page


def contacts_item_page(contact: ContactModel) -> rx.Component:
    return rx.box(
        rx.heading(contact.first_name),
        rx.text(contact.message),
        padding="1em",
    )


@rx.page(route=navigation.routes.CONTACT_LIST_ROUTE, on_load=ContactState.list_contacts)
def contacts_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Contact List", size="9"),
            rx.foreach(
                iterable=ContactState.contacts,
                render_fn=contacts_item_page,
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
        )
    )


@rx.page(route=navigation.routes.CONTACT_ROUTE)
def contact_page() -> rx.Component:
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
