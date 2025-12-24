# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.teacher_list, name='teacher_list'),
#     path('add-teacher/', views.add_teacher, name='add_teacher'),
#     path('update_teacher/<str:id>', views.update_teacher, name='update'),
#     path('delete_teacher/<int:id>/', views.delete_teacher, name='delete'),
# ]



from django.urls import path
from . import views

urlpatterns = [
   
    path('teachers', views.teacher_list, name='all-teachers'),
    path('add-teacher/', views.add_teacher, name="addteacher"),
    path('update-teacher/<str:id>', views.update_teacher, name="update"),
    path('delete/<str:id>', views.delete_teacher, name="delete")

]