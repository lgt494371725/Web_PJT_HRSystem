from django.urls import path, include
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
    path('detail/delete_assignexp/<int:pk>/', views.delete_assignexp, name='delete_assignexp'),

    path('detail<int:pk>/',views.detail, name='detail'),
    path('dropdown_test/', views.dropdown_test, name='test'),
    path('all_skills/', views.all_skills, name='all_skills'),
    path('all_skillCategories/', views.all_skillCategories, name='all_skillCategories'),
    path('all_careerLevels/', views.all_careerLevels, name='all_careerLevels'),
    path('all_industries/', views.all_industries, name='all_industries'),
    path('all_homeoffices/', views.all_homeoffices, name='all_industries'),
    path('all_dtes/', views.all_dtes, name='all_dtes'),
    path('skills_in_categories/', views.skills_in_categories, name='skills_in_categories'),
    path('all_users/', views.all_users, name='all_users')
]
