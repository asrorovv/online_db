from django.urls import path
from .views import courses_view

urlpatterns = [
    path('course/', courses_view, name='course-list')
]