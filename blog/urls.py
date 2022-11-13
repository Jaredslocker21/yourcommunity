from . import views
from django.urls import path

urlpatterns = [
    path("", views.MemberList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('create_member/', views.create_member, name='create_member'),
    path('edit_member/<slug:slug>/', views.edit_member, name='edit_member'),
    path('<slug:slug>/', views.MemberDetail.as_view(), name='member_detail'),
    path('like/<slug:slug>', views.MemberLike.as_view(), name='member_like'),
]
