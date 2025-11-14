from django.urls import include, path

urlpatterns = [
    path('auth/', include('api.v1.auth.urls')),
    path('users/', include('api.v1.users.urls')),
    path('courses/', include('api.v1.courses.urls')),
]
