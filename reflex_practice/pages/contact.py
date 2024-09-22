import asyncio

import reflex as rx

from reflex_practice import navigation
from reflex_practice.ui.base import base_page


class ContactState(rx.State):
    form_data: dict = {}
    did_submit: bool = False

    async def handle_submit(self, form_data: dict):
        print(form_data)
        self.form_data = form_data
        self.did_submit = True
        yield
        await asyncio.sleep(2)
        self.did_submit = False
        yield

    @rx.var
    def thank_you(self):
        first_name = self.form_data.get("first_name", "")
        return f"Thank you {first_name}".strip() + "!"


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
                    width="100%",
                ),
                width="100%",
            ),
            rx.input(
                placeholder="Email",
                name="email",
                type="email",
                width="100%",
            ),
            rx.text_area(
                placeholder="Message",
                name="message",
                width="100%",
            ),
            rx.button("Submit", type="submit"),
        ),
        on_submit=ContactState.handle_submit,
        reset_on_submit=True,
    )
    my_child = rx.vstack(
        rx.heading("Contact Us", size="9"),
        rx.cond(
            ContactState.did_submit,
            ContactState.thank_you,
            "",
        ),
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
