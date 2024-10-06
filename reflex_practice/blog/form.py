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
                name="content",
                width="100%",
            ),
            rx.button("Submit", type="submit"),
        ),
        on_submit=BlogPostState.create_post,
        reset_on_submit=True,
    )