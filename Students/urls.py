from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('view/<int:pk>', views.student_view, name='student_view'),
    path('new', views.student_create, name='student_new'),
    path('edit/<int:pk>', views.student_update, name='student_edit'),
    path('delete/<int:pk>', views.student_delete, name='student_delete'),
]