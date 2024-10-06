import reflex as rx

from reflex_practice import navigation


class NavState(rx.State):
    def to_home(self):
        return rx.redirect(navigation.routes.HOME_ROUTE)

    def to_about(self):
        return rx.redirect(navigation.routes.ABOUT_ROUTE)

    def to_pricing(self):
        return rx.redirect(navigation.routes.PRICING_ROUTE)

    def to_contact(self):
        return rx.redirect(navigation.routes.CONTACT_ROUTE)

    def to_blog(self):
        return rx.redirect(navigation.routes.BLOG_POSTS_ROUTE)

    def to_blog_detail(self, post_id: int):
        return rx.redirect(navigation.routes.BLOG_POSTS_ROUTE + f"/{post_id}")

    def to_blog_add_post(self):
        return rx.redirect(navigation.routes.CREATE_BLOG_POST_ROUTE)
