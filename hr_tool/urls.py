from django.urls import path
from . import views

app_name = 'hr_tool'

urlpatterns = [
    # path('', views.index, name='index'),
    path('list/', views.employee_list, name='list'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('detail/<str:pk>/add_precareer/', views.add_precareer, name='add_pre_career'),
    path('detail/<str:pk>/update_precareer/', views.update_precareer, name='update_pre_career'),
    path('detail/<str:pk>/precareer/', views.precareer, name='pre_career'),
    path('detail/<str:pk>/delete_precareer/', views.delete_precareer, name='delete_pre_career'),
    path('detail/<str:pk>/add_assignexp/', views.add_assignexp, name='add_assign_exp'),
    path('detail/<str:pk>/update_assignexp/', views.update_assignexp, name='update_assign_exp'),
    path('detail/<str:pk>/assignexp/', views.assignexp, name='assign_exp'),
    path('detail/<str:pk>/delete_assignexp/', views.delete_assignexp, name='delete_assign_exp')
]
