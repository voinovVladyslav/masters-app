from django.urls import path

from api.v1.users import views

urlpatterns = [
    path('', views.UserListApi.as_view(), name='user-list'),
    path('self/', views.UserSelfApi.as_view(), name='user-self'),
    path('create/', views.UserCreateApi.as_view(), name='user-create'),
]
