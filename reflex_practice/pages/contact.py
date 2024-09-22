import reflex as rx

from reflex_practice import navigation
from reflex_practice.ui.base import base_page


class ContactState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        print(self.form_data)


@rx.page(route=navigation.routes.CONTACT_ROUTE)
def contact_page() -> rx.Component:
    my_form = rx.form(
        rx.vstack(
            rx.hstack(
                rx.input(
                    placeholder="First Name",
                    name="first_name",
                    required=True,
                    width="100%",
                ),
                rx.input(
                    placeholder="Last Name",
                    name="last_name",
                    required=True,
                    width="100%",
                ),
                width="100%",
            ),
            rx.input(
                placeholder="Email",
                name="email",
                type="email",
                required=True,
                width="100%",
            ),
            rx.text_area(
                placeholder="Message",
                name="message",
                required=True,
                width="100%",
            ),
            rx.button("Submit", type="submit"),
        ),
        on_submit=ContactState.handle_submit,
        reset_on_submit=True,
    )
    my_child = rx.vstack(
        rx.heading("Contact Us", size="9"),
        rx.desktop_only(
            rx.box(
                my_form,
                id="my-form-box",
                width="50vw",
            )
        ),
        rx.tablet_only(
            rx.box(
                my_form,
                id="my-form-box",
                width="75vw",
            )
        ),
        rx.mobile_only(
            rx.box(
                my_form,
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
