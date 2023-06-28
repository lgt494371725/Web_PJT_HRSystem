from django.urls import path
from . import views

app_name = 'hr_tool'

urlpatterns = [
    path('analysis/', views.analysis, name='analysis'),
]
