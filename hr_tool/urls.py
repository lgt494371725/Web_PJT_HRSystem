from django.urls import path
from . import views

app_name = 'hr_tool'

urlpatterns = [
    # path('', views.index, name='index'),
    path('list/', views.employee_list, name='list'),
    path('dropdown_test/', views.dropdown_test, name='test'),
    path('all_skills/', views.all_skills, name='all_skills'),
    path('all_skillCategories/', views.all_skillCategories, name='all_skillCategories'),
    path('all_careerLevels/', views.all_careerLevels, name='all_careerLevels'),
    path('all_industries/', views.all_industries, name='all_industries'),
    path('all_homeoffices/', views.all_homeoffices, name='all_industries'),
    path('all_dtes/', views.all_dtes, name='all_dtes'),
    path('skills_in_categories/', views.skills_in_categories, name='skills_in_categories')
]
