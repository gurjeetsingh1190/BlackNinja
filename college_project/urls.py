
from django.contrib import admin
from .views import home,contact
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('course/',include("course.urls")),
    path('fees/',include("fee.urls"))
]
