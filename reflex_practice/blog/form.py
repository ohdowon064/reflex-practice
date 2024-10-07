import reflex as rx

from reflex_practice.blog.state import BlogPostState


def blog_post_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.input(
                placeholder="Subject",
                name="subject",
                type="text",
                required=True,
                width="100%",
            ),
            rx.text_area(
                placeholder="Content",
                height="50vh",
                name="content",
                width="100%",
            ),
            rx.flex(
                rx.switch(default_checked=True, name="publish_active"),
                rx.text("Publish Active"),
                spacing="2",
            ),
            rx.button("Submit", type="submit"),
            align="center",
        ),
        on_submit=BlogPostState.create_post,
        reset_on_submit=True,
    )
