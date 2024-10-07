import reflex as rx
import reflex_local_auth

from reflex_practice import navigation
from reflex_practice.blog.edit import edit_blog_post_page
from reflex_practice.blog.page import (
    blog_posts_page,
    blog_post_detail_page,
    create_blog_post_page,
)
from reflex_practice.blog.state import BlogPostState
from reflex_practice.contact.page import create_contact_page, contacts_page
from reflex_practice.contact.state import ContactState
from reflex_practice.pages.about import about_page
from reflex_practice.pages.pricing import pricing_page
from reflex_practice.ui.base import base_page
from rxconfig import config


class State(rx.State):
    label = "Welcome to Reflex!"

    def on_change(self, value: str) -> None:
        self.label = value

    def on_click(self):
        return rx.redirect(navigation.routes.ABOUT_ROUTE)


def index() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading(State.label, size="9"),
            rx.text(
                "Let's build something cool with Reflex! ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.input(
                default_value=State.label,
                on_click=State.on_click,
                on_change=State.on_change,
            ),
            rx.link(rx.button("About us"), href=navigation.routes.ABOUT_ROUTE),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id="my-child",
        )
    )


app = rx.App()
app.add_page(index)
# reflex-local-auth page
app.add_page(
    reflex_local_auth.pages.login_page,
    route=reflex_local_auth.routes.LOGIN_ROUTE,
    title="Login",
)
app.add_page(
    reflex_local_auth.pages.register_page,
    route=reflex_local_auth.routes.REGISTER_ROUTE,
    title="Register",
)

app.add_page(about_page, navigation.routes.ABOUT_ROUTE)
app.add_page(pricing_page, navigation.routes.PRICING_ROUTE)
app.add_page(create_contact_page, navigation.routes.CONTACT_ROUTE)
app.add_page(
    contacts_page,
    navigation.routes.CONTACTS_ROUTE,
    on_load=ContactState.list_contacts,
)
app.add_page(
    blog_posts_page,
    navigation.routes.BLOG_POSTS_ROUTE,
    on_load=BlogPostState.load_posts,
)
app.add_page(
    blog_post_detail_page,
    navigation.routes.BLOG_POST_DETAIL_ROUTE,
    on_load=BlogPostState.get_post,
)
app.add_page(
    edit_blog_post_page,
    navigation.routes.BLOG_POST_EDIT_ROUTE,
    on_load=BlogPostState.get_post,
)
app.add_page(create_blog_post_page, navigation.routes.CREATE_BLOG_POST_ROUTE)
