from django.shortcuts import render
from .models import MSkill,MSkillCategory,MCareerLevel,MIndustry,MHomeoffice,MDte
from .models import User
from .forms import SearchForm
from django.db import models
from django.http import JsonResponse
from django.forms.models import model_to_dict

# Create your views here.
def employee_list(request):
    form = SearchForm(request.GET)
    employees = User.objects.all() 
    print(form)
    if form.is_valid():
        query = form.cleaned_data['Search']
        print('abc',query)
        employees = User.objects.all() 
        employees = employees.filter(models.Q(id__icontains=query))
    else:
        print("!!!error:",form.errors)
        employees = User.objects.all() 
    context = {
        'employees':employees,
        'form': form
    }
    return render(request, 'list.html',context)

def detail(request, pk):
    return render(request, 'detail.html')




def to_json(queryset):
   return [model_to_dict(r) for r in queryset]

def all_skills(request):
    ret = MSkill.objects.all()
    return JsonResponse(to_json(ret),safe=False)

def all_skillCategories(request):
    ret = MSkillCategory.objects.all()
    return JsonResponse(to_json(ret),safe=False)

def skills_in_categories(request,category_id):
    ret = MSkill.objects.filter(skill_category=category_id)
    return JsonResponse(to_json(ret),safe=False)

def all_careerLevels(request):
    ret = MCareerLevel.objects.all()
    return JsonResponse(to_json(ret),safe=False)

def all_industries(request):
    ret = MIndustry.objects.all()
    return JsonResponse(to_json(ret),safe=False)

def all_dtes(request):
    ret = MDte.objects.all()
    return JsonResponse(to_json(ret),safe=False)

def all_homeoffices(request):
    ret = MHomeoffice.objects.all()
    return JsonResponse(to_json(ret),safe=False)

def dropdown_test(request):
   return render(request, 'dropdown_test.html')

def all_users(request):
   users = []
   for u in User.objects.all():
       users.append({'EID':u.id, 'DTE':u.dte.name,'ML':u.career_level.level,'Joining Date':u.join_of,'Home Office':u.homeoffice_id.name})
   return JsonResponse(users, safe=False)