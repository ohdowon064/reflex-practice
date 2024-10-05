import asyncio

import reflex as rx

from reflex_practice.contact.model import ContactEntryModel


class ContactState(rx.State):
    form_data: dict = {}
    did_submit: bool = False
    timeleft: int = 5

    @rx.var
    def timeleft_label(self):
        if self.timeleft < 1:
            return "No Time Left!"
        return f"{self.timeleft} seconds"

    async def handle_submit(self, form_data: dict):
        self.form_data = form_data
        with rx.session() as session:
            db_entry = ContactEntryModel(**form_data)
            print(db_entry)
            session.add(db_entry)
            session.commit()

        self.did_submit = True
        yield
        await asyncio.sleep(2)
        self.did_submit = False
        yield

    async def start_timer(self):
        while self.timeleft > 0:
            await asyncio.sleep(1)
            self.timeleft -= 1
            yield

    @rx.var
    def thank_you(self):
        first_name = self.form_data.get("first_name", "")
        return f"Thank you {first_name}".strip() + "!"
