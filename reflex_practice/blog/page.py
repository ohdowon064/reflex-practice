import reflex as rx

from reflex_practice.blog.model import BlogPostModel
from reflex_practice.blog.state import BlogPostState
from reflex_practice.ui.base import base_page


def blog_posts_item_page(blog_post: BlogPostModel) -> rx.Component:
    return rx.box(
        rx.heading(blog_post.subject),
        rx.text(blog_post.content),
        padding="1em",
    )


def blog_posts_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Blog Posts", size="9"),
            rx.foreach(
                iterable=BlogPostState.posts,
                render_fn=blog_posts_item_page,
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
        )
    )
