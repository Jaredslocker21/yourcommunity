from django.apps import AppConfig


# Model used from "I think therefore I blog" walkthrough.
class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
