import reflex as rx
from sqlmodel import select

from reflex_practice import navigation
from reflex_practice.blog.model import BlogPostModel


class BlogPostState(rx.State):
    post_data: dict = {}
    posts: list[BlogPostModel] = []
    post: BlogPostModel | None = None

    def load_posts(self):
        with rx.session() as session:
            query = select(BlogPostModel)
            posts = session.exec(query).all()
            self.posts = posts

    def get_post(self, post_id: int):
        pass

    def create_post(self, post_data: dict):
        with rx.session() as db_session:
            post = BlogPostModel(**post_data)
            db_session.add(post)
            db_session.commit()

        yield
        rx.redirect(navigation.routes.BLOG_POSTS_ROUTE)
