import reflex as rx
from sqlmodel import select

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

    def get_post(self):
        with rx.session() as session:
            if self.blog_post_id is None:
                self.post = None
                return
            query = select(BlogPostModel).where(BlogPostModel.id == self.blog_post_id)
            post = session.exec(query).one_or_none()
            self.post = post

    def create_post(self, post_data: dict):
        with rx.session() as db_session:
            post = BlogPostModel(**post_data)
            db_session.add(post)
            db_session.commit()

        yield

    @rx.var
    def blog_post_id(self):
        return self.router.page.params.get("post_id", None)
