import reflex as rx

from reflex_practice import navigation
from reflex_practice.blog.form import blog_post_form
from reflex_practice.blog.model import BlogPostModel
from reflex_practice.blog.state import BlogPostState
from reflex_practice.ui.base import base_page


def blog_post_title(post: BlogPostModel) -> rx.Component:
    child = rx.box(
        rx.heading(post.subject),
        padding="1em",
    )
    if post is None or post.id is None:
        return rx.fragment(child)
    return rx.link(
        child,
        href=f"{navigation.routes.BLOG_POSTS_ROUTE}/{post.id}",
    )


def blog_post_detail_page() -> rx.Component:
    can_edit = True
    post = BlogPostState.post
    edit_link = rx.link(
        rx.button("Edit"),
        href=BlogPostState.blog_post_edit_url,
    )
    edit_link_element = rx.cond(
        can_edit,
        edit_link,
        rx.fragment(),
    )
    my_child = rx.vstack(
        rx.hstack(
            rx.heading(post.subject, size="9"),
            edit_link_element,
            align="end",
        ),
        rx.text(post.content, white_space="pre-wrap"),
        spacing="5",
        align="center",
        min_height="85vh",
    )
    return base_page(my_child)


def create_blog_post_page() -> rx.Component:
    my_form = blog_post_form()
    my_child = rx.vstack(
        rx.heading("Create Blog Post", size="9"),
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


def blog_posts_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Blog Posts", size="9"),
            rx.link(
                rx.button("New Post"),
                href=navigation.routes.CREATE_BLOG_POST_ROUTE,
            ),
            rx.foreach(
                iterable=BlogPostState.posts,
                render_fn=blog_post_title,
            ),
            spacing="5",
            align="center",
            min_height="85vh",
        )
    )
