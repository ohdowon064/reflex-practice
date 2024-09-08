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
            rx.input(
                placeholder="First Name",
                name="first_name",
                required=True,
            ),
            rx.input(
                placeholder="Last Name",
                name="last_name",
                required=True,
            ),
            rx.input(
                placeholder="Email",
                name="email",
                type="email",
                required=True,
            ),
            rx.text_area(
                placeholder="Message",
                name="message",
                required=True,
            ),
            rx.button("Submit", type="submit"),
        ),
        on_submit=ContactState.handle_submit,
        reset_on_submit=True,
    )
    return base_page(my_form)
