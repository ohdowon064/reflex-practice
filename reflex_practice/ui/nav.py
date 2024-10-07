import reflex as rx
import reflex_local_auth

from reflex_practice import navigation


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(rx.text(text, size="4", weight="medium"), href=url)


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.link(
                        rx.image(
                            src="https://reflex.dev/logo.jpg",
                            width="2.25em",
                            height="auto",
                            border_radius="25%",
                        ),
                        href="/",
                    ),
                    rx.link(
                        rx.heading("Reflex", size="7", weight="bold"),
                        href="/",
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", navigation.routes.HOME_ROUTE),
                    navbar_link("About", navigation.routes.ABOUT_ROUTE),
                    navbar_link("Blog", navigation.routes.BLOG_POSTS_ROUTE),
                    navbar_link("Pricing", navigation.routes.PRICING_ROUTE),
                    navbar_link("Contact", navigation.routes.CONTACT_ROUTE),
                    spacing="5",
                ),
                rx.hstack(
                    rx.link(
                        rx.button(
                            "Sign Up",
                            size="3",
                            variant="outline",
                        ),
                        href=reflex_local_auth.routes.REGISTER_ROUTE,
                    ),
                    rx.link(
                        rx.button("Log In", size="3"),
                        href=reflex_local_auth.routes.LOGIN_ROUTE,
                    ),
                    spacing="4",
                    align_items="center",
                ),
                justify="between",
                align_items="center",
                id="my-navbar-hstack-desktop",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="https://reflex.dev/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("Reflex", size="6", weight="bold"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        rx.menu.item(
                            "Home", on_click=navigation.state.NavState.to_home
                        ),
                        rx.menu.item(
                            "About", on_click=navigation.state.NavState.to_about
                        ),
                        rx.menu.item(
                            "Blog", on_click=navigation.state.NavState.to_blog
                        ),
                        rx.menu.item(
                            "Pricing", on_click=navigation.state.NavState.to_pricing
                        ),
                        rx.menu.item(
                            "Contact", on_click=navigation.state.NavState.to_contact
                        ),
                        rx.menu.separator(),
                        rx.menu.item(
                            "Log in", on_click=navigation.state.NavState.to_login
                        ),
                        rx.menu.item(
                            "Sign up", on_click=navigation.state.NavState.to_register
                        ),
                    ),
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        width="100%",
        id="my-main-nav",
    )
