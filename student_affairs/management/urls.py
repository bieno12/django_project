from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),
    path('student/list', views.student_list, name="student_list"),
    path('student/add', views.student_add, name="student_add"),
    path('student/edit/<int:id>', views.student_edit, name="student_edit"),
    path('department/list', views.departments, name="departments"),
    path('student/search', views.search, name="search"),
    path('about/', views.about, name="about"),
]




