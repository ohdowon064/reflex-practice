import asyncio

import reflex as rx
from sqlmodel import select

from reflex_practice.contact.model import ContactModel


class ContactState(rx.State):
    form_data: dict = {}
    did_submit: bool = False
    contacts: list[ContactModel] = []

    async def handle_submit(self, form_data: dict):
        self.form_data = form_data
        with rx.session() as session:
            db_entry = ContactModel(**form_data)
            session.add(db_entry)
            session.commit()

        self.did_submit = True
        yield
        await asyncio.sleep(2)
        self.did_submit = False
        yield

    @rx.var
    def thank_you(self):
        first_name = self.form_data.get("first_name", "")
        return f"Thank you {first_name}".strip() + "!"

    def list_contacts(self) -> None:
        with rx.session() as session:
            query = select(ContactModel)
            contacts = session.exec(query).all()
            self.contacts = contacts
