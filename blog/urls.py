from . import views
from django.urls import path

urlpatterns = [
    path("", views.MemberList.as_view(), name='home'),
    path('<slug:slug>/', views.MemberDetail.as_view(), name='member_detail'),
    path('like/<slug:slug>', views.MemberLike.as_view(), name='member_like'),
    path('about/', views.about, name='about'),
]
