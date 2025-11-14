from django.urls import path

from api.v1.courses import views

urlpatterns = [
    path('', views.CourseListApi.as_view(), name='course-list'),
    path('<int:pk>/', views.CourseDetailApi.as_view(), name='course-detail'),
]
