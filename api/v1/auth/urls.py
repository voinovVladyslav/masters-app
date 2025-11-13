from django.urls import path

from api.v1.auth import views

urlpatterns = [
    path('token/', views.ObtainTokenApi.as_view(), name='token-obtain'),
]
