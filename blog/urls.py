from . import views
from django.urls import path

urlpatterns = [
    path("", views.MemberList.as_view(), name='home'),
]
