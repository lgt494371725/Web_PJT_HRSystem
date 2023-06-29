from django.urls import path
from . import views

app_name = 'hr_tool'

urlpatterns = [
    # path('', views.index, name='index'),
    path('list/', views.employee_list, name='list'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('analysis/', views.analysis, name='analysis'),
    path('download-file/', views.download_file_view, name='download_file'),
]
