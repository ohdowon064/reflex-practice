import reflex as rx
from sqlmodel import select

from reflex_practice.blog.model import BlogPostModel


class BlogPostState(rx.State):
    posts: list[BlogPostModel] = []
    post: BlogPostModel | None = None

    def load_posts(self):
        with rx.session() as session:
            query = select(BlogPostModel)
            posts = session.exec(query).all()
            self.posts = posts

    def get_post(self, post_id: int):
        pass
