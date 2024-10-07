from datetime import datetime, timezone

import reflex as rx

from reflex_practice.blog.model import BlogPostModel
from reflex_practice.blog.state import BlogPostState
from reflex_practice.ui.base import base_page


class BlogPostEditFormState(BlogPostState):
    @rx.var
    def publish_display_date(self) -> str:
        if self.post is None or self.post.publish_datetime is None:
            return datetime.now().strftime("%Y-%m-%d")
        return self.post.publish_datetime.strftime("%Y-%m-%d")

    @rx.var
    def publish_display_time(self) -> str:
        if self.post is None or self.post.publish_datetime is None:
            return datetime.now().strftime("%H:%M")
        return self.post.publish_datetime.strftime("%H:%M")

    def handle_submit(self, form_data: dict):
        post_id = self.router.page.params.get("post_id", None)
        if post_id is None:
            return
        form_data["publish_active"] = form_data.get("publish_active", False) == "on"
        pub_date = form_data.pop("publish_date", "")
        pub_time = form_data.pop("publish_time", "")
        publish_datetime = f"{pub_date} {pub_time}"
        try:
            form_data["publish_datetime"] = datetime.strptime(
                publish_datetime, "%Y-%m-%d %H:%M"
            ).astimezone(timezone.utc)
        except:
            form_data["publish_datetime"] = None
        print(form_data)
        BlogPostModel.update(post_id, form_data)
        return self.to_blog_post_detail()


def blog_post_edit_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.input(
                default_value=BlogPostEditFormState.post_subject,
                on_change=BlogPostEditFormState.set_post_subject,
                placeholder="Subject",
                name="subject",
                type="text",
                required=True,
                width="100%",
            ),
            rx.text_area(
                value=BlogPostEditFormState.post_content,
                on_change=BlogPostEditFormState.set_post_content,
                placeholder="Content",
                height="50vh",
                name="content",
                width="100%",
            ),
            rx.flex(
                rx.switch(
                    default_checked=BlogPostEditFormState.post_publish_active,
                    on_change=BlogPostEditFormState.set_post_publish_active,
                    name="publish_active",
                ),
                rx.text("Publish Active"),
                spacing="2",
            ),
            rx.cond(
                BlogPostEditFormState.post_publish_active,
                rx.box(
                    rx.hstack(
                        rx.input(
                            default_value=BlogPostEditFormState.publish_display_date,
                            type="date",
                            name="publish_date",
                            width="100%",
                        ),
                        rx.input(
                            default_value=BlogPostEditFormState.publish_display_time,
                            type="time",
                            name="publish_time",
                            width="100%",
                        ),
                    ),
                    width="100%",
                ),
            ),
            rx.button("Submit", type="submit"),
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
