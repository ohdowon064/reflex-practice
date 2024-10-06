import reflex as rx

from reflex_practice import navigation
from reflex_practice.blog.model import BlogPostModel
from reflex_practice.blog.state import BlogPostState
from reflex_practice.ui.base import base_page


def blog_post_page(blog_post: BlogPostModel) -> rx.Component:
    return rx.box(
        rx.heading(blog_post.subject),
        padding="1em",
    )


def blog_post_detail_page(child: rx.Component, post: BlogPostModel) -> rx.Component:
    if post is None or post.id is None:
        return rx.fragment(child)
    return rx.link(
        child,
        href=f"{navigation.routes.BLOG_POSTS_ROUTE}/{post.id}",
    )


def blog_posts_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Blog Posts", size="9"),
            rx.foreach(
                iterable=BlogPostState.posts,
                render_fn=blog_post_page,
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
        )
    )
