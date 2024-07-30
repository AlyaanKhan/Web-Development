# student_management/urls.py
from django.contrib import admin
from django.urls import path, include
from students import views as student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('students.urls')),
    path('', student_views.index, name='index'),
    path('register/', student_views.register, name='register'),
    path('login/', student_views.login_user, name='login'),
    path('logout/', student_views.logout_user, name='logout'),
]
