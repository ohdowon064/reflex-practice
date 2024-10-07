import reflex as rx
from sqlmodel import select

from reflex_practice import navigation
from reflex_practice.blog.model import BlogPostModel


class BlogPostState(rx.State):
    posts: list[BlogPostModel] = []
    post: BlogPostModel | None = None
    post_subject: str = ""
    post_content: str = ""
    post_publish_active: bool = False

    def load_posts(self):
        self.posts = BlogPostModel.find_all()

    def get_post(self):
        post_id = self.blog_post_id
        if post_id is None:
            self.post = None
            return
        self.post = BlogPostModel.find_one(post_id)
        self.post_subject = self.post.subject
        self.post_content = self.post.content
        self.post_publish_active = self.post.publish_active

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
        self.post = BlogPostModel.create(post_data)
        return self.to_blog_post_detail()

    @rx.var
    def blog_post_id(self) -> int | None:
        return self.router.page.params.get("post_id", None)
