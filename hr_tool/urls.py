from django.urls import path
from . import views

app_name = 'hr_tool'

urlpatterns = [
    # path('', views.index, name='index'),
    path('list/', views.employee_list, name='list'),
    path('detail/<str:pk>/', views.detail, name='detail'),
    path('analysis/', views.analysis, name='analysis'),
    path('download-file/', views.download_file_view, name='download_file'),
    path('detail/<str:pk>/edit_precareer/', views.edit_precareer, name='edit_precareer'),
    path('detail/<str:pk>/add_precareer/', views.add_precareer, name='add_precareer'),
    path('detail/update_precareer/<int:pk>/', views.update_precareer, name='update_precareer'),
    path('detail/delete_precareer/<int:pk>/', views.delete_precareer, name='delete_precareer'),
    path('detail/<str:pk>/edit_assignexp/', views.edit_assignexp, name='edit_assignexp'),
    path('detail/<str:pk>/add_assignexp/', views.add_assignexp, name='add_assignexp'),
    path('detail/update_assignexp/<int:pk>/', views.update_assignexp, name='update_assignexp'),
    path('detail/delete_assignexp/<int:pk>/', views.delete_assignexp, name='delete_assignexp')
]