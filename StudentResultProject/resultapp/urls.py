from django.urls import path
from . import views

app_name = 'resultapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),  
    path('logout/', views.logout_view, name='logout'),
    path('students/', views.student_list, name='student_list'),
    path('add-student/', views.add_student, name='add_student'),
    path('add-marks/<int:student_id>/', views.add_marks, name='add_marks'),
    path('result/<int:student_id>/', views.view_result, name='view_result'),
]