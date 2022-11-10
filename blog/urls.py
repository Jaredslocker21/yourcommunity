from . import views
from django import path

urlpatterns = [
    path('', views.MemberList.as_view(), name='home')
]