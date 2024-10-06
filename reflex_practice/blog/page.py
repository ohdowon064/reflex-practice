import reflex as rx

from reflex_practice import navigation
from reflex_practice.blog.form import blog_post_form
from reflex_practice.blog.model import BlogPostModel
from reflex_practice.blog.state import BlogPostState
from reflex_practice.ui.base import base_page


def blog_post_page(blog_post: BlogPostModel) -> rx.Component:
    child = rx.box(
        rx.heading(blog_post.subject),
        padding="1em",
    )
    return redirect_blog_post_page(child, blog_post)


def redirect_blog_post_page(child: rx.Component, post: BlogPostModel) -> rx.Component:
    if post is None or post.id is None:
        return rx.fragment(child)
    return rx.link(
        child,
        href=f"{navigation.routes.BLOG_POSTS_ROUTE}/{post.id}",
    )


def blog_post_detail_page() -> rx.Component:
    my_child = rx.vstack(
        rx.heading(BlogPostState.post.subject, size="9"),
        rx.text(BlogPostState.post.content),
        spacing="5",
        align="center",
        min_height="85vh",
    )
    return base_page(my_child)


def create_blog_post_page() -> rx.Component:
    my_child = rx.vstack(
        rx.heading("Create Blog Post", size="9"),
        rx.desktop_only(
            rx.box(
                blog_post_form(),
                id="my-form-box",
                width="50vw",
            )
        ),
        rx.tablet_only(
            rx.box(
                blog_post_form(),
                id="my-form-box",
                width="75vw",
            )
        ),
        rx.mobile_only(
            rx.box(
                blog_post_form(),
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
            rx.button(
                "Create New Post",
                on_click=rx.redirect(navigation.routes.CREATE_BLOG_POST_ROUTE),
            ),
            rx.foreach(
                iterable=BlogPostState.posts,
                render_fn=blog_post_page,
            ),
            spacing="5",
            align="center",
            min_height="85vh",
        )
    )
