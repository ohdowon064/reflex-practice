import reflex as rx

from reflex_practice import navigation
from reflex_practice.blog.model import BlogPostModel
from reflex_practice.blog.state import BlogPostState
from reflex_practice.ui.base import base_page


class BlogPostEditFormState(BlogPostState):
    def handle_submit(self, form_data: dict):
        post_id = self.router.page.params.get("post_id", None)
        if post_id is None:
            return

        with rx.session() as db_session:
            query = BlogPostModel.select().where(BlogPostModel.id == post_id)
            post = db_session.exec(query).one_or_none()
            if post is None:
                return
            for key, value in form_data.items():
                setattr(post, key, value)
            db_session.add(post)
            db_session.commit()
        return navigation.state.NavState.to_blog_detail(post_id)


def blog_post_edit_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.input(
                default_value=BlogPostEditFormState.post.subject,
                placeholder="Subject",
                name="subject",
                type="text",
                required=True,
                width="100%",
            ),
            rx.text_area(
                value=BlogPostEditFormState.post.content,
                placeholder="Content",
                height="50vh",
                name="content",
                width="100%",
            ),
            rx.button("Submit", type="submit"),
            align="center",
        ),
        on_submit=BlogPostEditFormState.handle_submit,
    )


def edit_blog_post_page() -> rx.Component:
    my_form = blog_post_edit_form()
    my_child = rx.vstack(
        rx.heading("Edit Blog Post", size="9"),
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
        align="center",
        justify="center",
        min_height="85vh",
    )
    return base_page(my_child)
