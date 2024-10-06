import reflex as rx
from sqlmodel import select

from reflex_practice import navigation
from reflex_practice.blog.model import BlogPostModel


class BlogPostState(rx.State):
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

    @rx.var
    def blog_post_edit_url(self) -> str:
        if self.post is None:
            return navigation.routes.BLOG_POSTS_ROUTE
        return f"{navigation.routes.BLOG_POSTS_ROUTE}/{self.post.id}/edit"

    def to_blog_post_detail(self, edit_mode: bool = False):
        if self.post is None:
            return rx.redirect(navigation.routes.BLOG_POSTS_ROUTE)
        if edit_mode:
            return rx.redirect(self.blog_post_edit_url)
        return rx.redirect(navigation.routes.BLOG_POSTS_ROUTE + f"/{self.post.id}")

    def create_post(self, post_data: dict):
        with rx.session() as db_session:
            post = BlogPostModel(**post_data)
            db_session.add(post)
            db_session.commit()
            db_session.refresh(post)
            self.post = post
            return self.to_blog_post_detail()

    @rx.var
    def blog_post_id(self):
        return self.router.page.params.get("post_id", None)
