from django.urls import path
from .views import course_list, apply_course

urlpatterns = [
    path('', course_list, name='course_list'),
    path('<int:course_id>/apply/', apply_course, name='apply_course')]