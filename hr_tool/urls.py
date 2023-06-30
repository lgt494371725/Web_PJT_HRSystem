from django.urls import path
from . import views

app_name = 'hr_tool'

urlpatterns = [
    # path('', views.index, name='index'),
    path('list/', views.employee_list, name='list'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('detail/<str:pk>/edit_precareer/', views.edit_precareer, name='edit_pre_career'),
    path('detail/<str:pk>/add_precareer/', views.add_precareer, name='add_pre_career'),
    path('detail/<str:pk>/edit_skill/', views.edit_skill, name='edit_skill'),
    path('detail/<str:pk>/add_skill/', views.add_skill, name='add_skill'),
    path('detail/<str:pk>/update_skill/', views.update_skill, name='update_skill'),
]
