from django.urls import path
from . import views

urlpatterns = [
   
    path('students', views.student_list, name='all-students'),
    path('add-student/', views.add_student, name="addstudent"),
    path('update-student/<str:id>', views.update_student, name="update"),
    path('delete/<str:id>', views.delete_student, name="delete")

]